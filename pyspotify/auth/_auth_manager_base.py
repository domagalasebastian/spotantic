import asyncio
import webbrowser
from abc import ABC
from abc import abstractmethod
from typing import Optional
from urllib.parse import urlencode
from urllib.parse import urlparse

from aiohttp import BasicAuth
from aiohttp import ClientSession
from aiohttp import web

from pyspotify._utils.auth import generate_url_safe_token
from pyspotify._utils.logger import logger
from pyspotify.models.auth import AccessTokenInfo
from pyspotify.models.auth import AccessTokenRequestBody
from pyspotify.models.auth import AuthCodeRequestParams
from pyspotify.models.auth import AuthSettings

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
ACCESS_TOKEN_REQUEST_CONTENT_TYPE = "application/x-www-form-urlencoded"


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
            ValueError: If the access token has never been obtained.
        """
        if self._access_token_info is None:
            raise ValueError("Access token data is unknown!")

        return self._access_token_info

    async def _get_auth_code(self, params: AuthCodeRequestParams) -> str:
        """Retrieve an authorization code from the user.

        Starts a local HTTP server to receive the callback with the authorization code,
        opens the user's browser to the Spotify authorization endpoint, and waits for
        the user to grant permission.

        Args:
            params: Parameters for the authorization request.

        Returns:
            The authorization code provided by Spotify.

        Raises:
            Exception: If the state validation fails or if the server setup fails.
        """
        code = None
        state = generate_url_safe_token(32)
        params_dict = params.model_dump(mode="json", exclude_none=True)
        params_dict["state"] = state
        redirect_uri = str(params.redirect_uri)

        self._logger.info(f"Waiting for authorization code at: {redirect_uri}")
        self._logger.debug(f"Authorization redirect URI: {redirect_uri}")

        async def callback(request) -> web.Response:
            nonlocal code
            r_state = request.query.get("state")
            if r_state != state:
                raise Exception("State mismatch in OAuth callback response.")

            code = request.query.get("code")
            return web.Response(text="OK")

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

            while code is None:
                await asyncio.sleep(1)
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
        and optional authentication header.

        Args:
            request_body: The request body containing grant type and flow-specific parameters.
            auth: Optional HTTP Basic Authentication credentials for the token request.

        Returns:
            Object containing the access token and its metadata.

        Raises:
            Exception: If the token request returns a non-200 status code.
        """
        self._logger.info("Receiving access token from the server.")
        self._logger.debug(f"Requesting access token with data: {request_body}")

        headers = {
            "Content-Type": ACCESS_TOKEN_REQUEST_CONTENT_TYPE,
        }
        data = request_body.model_dump(mode="json", exclude_none=True)
        async with ClientSession() as session:
            async with session.post(TOKEN_URL, headers=headers, auth=auth, data=data) as response:
                payload = await response.json()
                if response.status != 200:
                    raise Exception(f"Failed to obtain access token (status={response.status}): {payload}")

        token_info = AccessTokenInfo(**payload)

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
        self._refresh_event = None
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
            raise ValueError("Access token data is unknown!")

        if self._access_token_info.is_expired():
            if self._allow_lazy_refresh:
                await self._atomic_refresh()
            else:
                self._logger.warning("The token has expired! It is no longer valid!")

        return self._access_token_info

    async def _atomic_refresh(self) -> None:
        """Ensure that the refresh task is run only once at a time.

        Returns:
            None
        """
        if self._lock.locked() and self._refresh_event is not None:
            self._logger.debug("Token refresh is already in progress!")
            await self._refresh_event.wait()
            return

        async with self._lock:
            self._refresh_event = asyncio.Event()
            await self.refresh()
            self._refresh_event.set()
            self._refresh_event = None
