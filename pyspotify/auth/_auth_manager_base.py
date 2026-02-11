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

    def __init__(self, auth_settings: AuthSettings) -> None:
        """Initialize the authentication manager.

        Args:
            auth_settings: Configuration settings including client credentials and other flow-specific parameters.
        """
        self.__auth_settings = auth_settings
        self._logger = logger.getChild("auth")

    @property
    def auth_settings(self) -> AuthSettings:
        """Get the current authentication settings.

        Returns:
            The authentication configuration.
        """
        return self.__auth_settings

    @auth_settings.setter
    def auth_settings(self, value: AuthSettings) -> None:
        """Set the authentication settings.

        Args:
            value: The new authentication configuration.
        """
        self.__auth_settings = value

    @abstractmethod
    async def authorize(self) -> AccessTokenInfo:
        """Authorize and obtain an access token.

        This method must be implemented by subclasses to handle the specific
        OAuth2 flow logic.

        Returns:
            Object containing the access token and its metadata.
        """

    async def get_auth_code(self, params: AuthCodeRequestParams) -> str:
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

        self._logger.info(f"Receiving auth code. Redirect URI: {redirect_uri}")
        self._logger.debug(f"Authorization request params: {params}")

        async def callback(request) -> web.Response:
            nonlocal code
            r_state = request.query.get("state")
            if r_state != state:
                raise Exception("Wrong state received in reponse!")

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

    async def get_access_token(
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
                    raise Exception(f"Failed to get access token! Payload: {payload}")

        token_info = AccessTokenInfo(**payload)

        if self.auth_settings.store_access_token:
            self._logger.info(f"Saving access token to file: {self.auth_settings.access_token_file_path}")
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info


class RefreshableAuthManager(AuthManagerBase, ABC):
    """Abstract base class for refreshable authentication flows.

    Extends AuthManagerBase for OAuth2 flows that support token refresh functionality,
    allowing access tokens to be renewed without user re-authentication.
    """

    @abstractmethod
    async def refresh(self, refresh_token: str) -> AccessTokenInfo:
        """Refresh an expired access token.

        This method must be implemented by subclasses to handle the specific
        refresh logic for their OAuth2 flow.

        Args:
            refresh_token: The refresh token obtained during authorization.

        Returns:
            Object containing the new access token and its metadata.
        """
