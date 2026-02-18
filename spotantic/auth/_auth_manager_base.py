import asyncio
import time
import webbrowser
from abc import ABC
from abc import abstractmethod
from http import HTTPStatus
from typing import Optional
from urllib.parse import urlencode
from urllib.parse import urlparse

from aiohttp import BasicAuth
from aiohttp import ClientSession
from aiohttp import web

from spotantic._utils.auth import generate_url_safe_token
from spotantic._utils.logger import logger
from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import AccessTokenRequestBody
from spotantic.models.auth import AuthCodeRequestParams
from spotantic.models.auth import AuthSettings
from spotantic.types.exceptions import SpotanticAuthAccessTokenRequestError
from spotantic.types.exceptions import SpotanticAuthCodeRequestError
from spotantic.types.exceptions import SpotanticAuthSecurityError

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
ACCESS_TOKEN_REQUEST_CONTENT_TYPE = "application/x-www-form-urlencoded"
AUTH_CODE_REQUEST_TIMEOUT_SECS = 60


class AuthManagerBase(ABC):
    """Abstract base class for Spotify OAuth2 authentication managers.

    Provides common functionality for different OAuth2 flows including token acquisition and management.
    """

    def __init__(self, auth_settings: AuthSettings, access_token_info: Optional[AccessTokenInfo] = None) -> None:
        """Initialize the authentication manager.

        Args:
            auth_settings: Configuration settings including client credentials and other flow-specific parameters.
            access_token_info: Access token info loaded from cache, if any.
        """
        self._access_token_info = access_token_info
        self._auth_settings = auth_settings
        self._logger = logger.getChild("auth")

    @property
    def auth_settings(self) -> AuthSettings:
        """Get the current authentication settings.

        Returns:
            The authentication configuration.
        """
        return self._auth_settings

    @auth_settings.setter
    def auth_settings(self, value: AuthSettings) -> None:
        """Set the authentication settings.

        Args:
            value: The new authentication configuration.
        """
        self._auth_settings = value

    @abstractmethod
    async def authorize(self) -> None:
        """Authorize and obtain an access token.

        This method must be implemented by subclasses to handle the specific
        OAuth2 flow logic.

        Returns:
            None
        """

    async def get_valid_access_token(self) -> AccessTokenInfo:
        """Return the information about the access token, if exists.

        Returns:
            A valid access token object.

        Raises:
            ValueError: If the access token has never been obtained. Call authorize() first.
        """
        if self._access_token_info is None:
            raise ValueError(
                "No access token available. Call authorize() first to obtain a token through the OAuth2 flow."
            )

        return self._access_token_info

    async def _get_auth_code(self, params: AuthCodeRequestParams) -> str:
        """Retrieve an authorization code from the user.

        Starts a local HTTP server to receive the callback with the authorization code,
        opens the user's browser to the Spotify authorization endpoint, and waits for
        the user to grant permission. Includes CSRF protection via state parameter validation
        and enforces a timeout to prevent indefinite waiting.

        Args:
            params: Parameters for the authorization request.

        Returns:
            The authorization code provided by Spotify.

        Raises:
            SpotanticAuthSecurityError: If the state parameter doesn't match (CSRF validation failed).
            SpotanticAuthCodeRequestError: If the authorization request fails (user denied or error from Spotify).
            TimeoutError: If the authorization code is not received within the timeout period.
        """
        code = None
        auth_code_request_exc = None

        state = generate_url_safe_token(32)
        params_dict = params.model_dump(mode="json", exclude_none=True)
        params_dict["state"] = state
        redirect_uri = str(params.redirect_uri)

        self._logger.info(f"Opening browser for authorization. Listening for callback at {redirect_uri}")

        async def callback(request: web.Request) -> web.Response:
            """Handle the OAuth2 authorization callback from Spotify.

            This callback is called when the user grants permission and Spotify redirects
            back to the local server with the authorization code and state parameter.
            Validates the state parameter for CSRF protection and checks for authorization errors.

            Args:
                request: The incoming request containing code and state query parameters.

            Returns:
                A Response with status and message indicating the result of the callback.
                Status codes: 200 (OK) for success, 412 (Precondition Failed) for state mismatch,
                401 (Unauthorized) for authorization failure.
            """
            nonlocal code, auth_code_request_exc
            r_state = request.query.get("state")
            code = request.query.get("code", None)

            if r_state != state:
                text = f"State mismatch in OAuth callback! Expected {state}, got {r_state}"
                status = HTTPStatus.PRECONDITION_FAILED
                auth_code_request_exc = SpotanticAuthSecurityError(text)
            elif code is None:
                err = request.query.get("error", None) or "Reason unknown"
                text = f"Authorization Code Request failed! Server response: {err}"
                status = HTTPStatus.UNAUTHORIZED
                auth_code_request_exc = SpotanticAuthCodeRequestError(text)
            else:
                text = "Authorization Code Request completed successfully. You can close this tab now."
                status = HTTPStatus.OK

            return web.Response(text=text, status=status)

        target_url = f"{AUTH_URL}?{urlencode(params_dict)}"
        server_address_parsed = urlparse(redirect_uri)

        app = web.Application()
        app.router.add_get("/callback", callback)
        runner = web.AppRunner(app)
        await runner.setup()
        try:
            site = web.TCPSite(runner, host=server_address_parsed.hostname, port=server_address_parsed.port)
            await site.start()
        except Exception:
            raise
        else:
            webbrowser.open(target_url)

            timeout = time.time() + AUTH_CODE_REQUEST_TIMEOUT_SECS
            while time.time() < timeout:
                if auth_code_request_exc is not None:
                    raise auth_code_request_exc

                if code is not None:
                    break

                await asyncio.sleep(1)
            else:
                raise TimeoutError(
                    f"Authorization Code Request was not completed within {AUTH_CODE_REQUEST_TIMEOUT_SECS} seconds"
                )

        finally:
            await runner.cleanup()

        return code

    async def _get_access_token(
        self,
        *,
        request_body: AccessTokenRequestBody,
        auth: Optional[BasicAuth] = None,
    ) -> AccessTokenInfo:
        """Request an access token from Spotify's token server.

        Sends a POST request to Spotify's token endpoint with the provided data
        and optional authentication header. If configured, stores the obtained token
        to the file system for later retrieval.

        Args:
            request_body: The request body containing grant type and flow-specific parameters.
            auth: Optional HTTP Basic Authentication credentials for the token request.

        Returns:
            Object containing the access token and its metadata.

        Raises:
            SpotanticAuthAccessTokenRequestError: If the token request returns a non-200 status code.
        """
        self._logger.info(f"Requesting access token from Spotify token endpoint using {request_body.grant_type} flow")
        self._logger.debug(f"Token request parameters: {request_body}")

        headers = {
            "Content-Type": ACCESS_TOKEN_REQUEST_CONTENT_TYPE,
        }
        data = request_body.model_dump(mode="json", exclude_none=True)
        async with ClientSession() as session:
            async with session.post(TOKEN_URL, headers=headers, auth=auth, data=data) as response:
                if response.status != HTTPStatus.OK:
                    payload = await response.text()
                    raise SpotanticAuthAccessTokenRequestError(
                        f"Failed to obtain access token (status={response.status}): {payload}"
                    )

                access_token_data = await response.json()

        token_info = AccessTokenInfo(**access_token_data)

        if self._auth_settings.store_access_token:
            self._logger.info(f"Saving access token to file: {self._auth_settings.access_token_file_path}")
            token_info.store_token(file_path=self._auth_settings.access_token_file_path)

        return token_info


class RefreshableAuthManager(AuthManagerBase, ABC):
    """Abstract base class for refreshable authentication flows.

    Extends AuthManagerBase for OAuth2 flows that support token refresh functionality,
    allowing access tokens to be renewed without user re-authentication.
    """

    def __init__(
        self,
        auth_settings: AuthSettings,
        access_token_info: Optional[AccessTokenInfo] = None,
        allow_lazy_refresh: bool = False,
    ) -> None:
        """Initialize the authentication manager.

        Args:
            auth_settings: Configuration settings including client credentials and other flow-specific parameters.
            access_token_info: Access token info loaded from cache, if any.
            allow_lazy_refresh: If set, the expired token will be refreshed automatically before returning it.
        """
        self._lock = asyncio.Lock()
        self._allow_lazy_refresh = allow_lazy_refresh
        super(RefreshableAuthManager, self).__init__(auth_settings=auth_settings, access_token_info=access_token_info)

    @abstractmethod
    async def refresh(self) -> None:
        """Refresh an expired access token.

        This method must be implemented by subclasses to handle the specific
        refresh logic for their OAuth2 flow.

        Returns:
            None
        """

    async def get_valid_access_token(self) -> AccessTokenInfo:
        """Return the information about the access token, if exists.

        If lazy refreshing is allowed, the expired token will be refreshed automatically.

        Returns:
            A valid access token object.

        Raises:
            ValueError: If the access token has never been obtained.
        """
        if self._access_token_info is None:
            raise ValueError(
                "No access token available. Call authorize() first to obtain a token through the OAuth2 flow."
            )

        if self._access_token_info.is_expired():
            if self._allow_lazy_refresh:
                # Atomically refresh the access token, preventing concurrent refresh attempts.
                async with self._lock:
                    if not self._access_token_info.is_expired():
                        return self._access_token_info

                    await self.refresh()
            else:
                self._logger.warning(
                    "Access token has expired. Call authorize() to refresh the token or enable "
                    "allow_lazy_refresh=True for automatic refresh."
                )

        return self._access_token_info
