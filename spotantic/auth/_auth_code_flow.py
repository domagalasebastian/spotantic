from spotantic.models.auth import AccessTokenRequestBody
from spotantic.models.auth import AuthCodeRequestParams

from ._auth_manager_base import RefreshableAuthManager

AUTH_CODE_FLOW_GRANT_TYPE = "authorization_code"
AUTH_CODE_FLOW_RESPONSE_TYPE = "code"
REFRESH_AUTH_CODE_FLOW_GRANT_TYPE = "refresh_token"


class AuthCodeFlowManager(RefreshableAuthManager):
    """Manager for Spotify OAuth2 Authorization Code Flow.

    The authorization code flow is suitable for long-running applications (e.g. web and mobile apps)
    where the user grants permission only once.

    This flow requires user interaction to grant permission and returns both an access token
    and a refresh token for long-term access. For more information refer to:
    `Authorization Code Flow <https://developer.spotify.com/documentation/web-api/tutorials/code-flow>`_.
    """

    async def authorize(self) -> None:
        """Authorize using the Authorization Code Flow.

        Initiates the authorization process by redirecting the user to Spotify's authorization
        endpoint. The user grants permission, and the authorization code is exchanged for an
        access token and refresh token.

        Returns:
            None

        Raises:
            ValueError: If any required settings (`client_id`, `client_secret`, `redirect_uri`, `scope`) are not set.
        """
        self._logger.info("Starting Authorization Code Flow")
        self._logger.debug(f"Current auth settings: {self._auth_settings}")

        if self._auth_settings.client_id is None:
            raise ValueError("Client ID must be set for Authorization Code Flow")

        if self._auth_settings.client_secret is None:
            raise ValueError("Client Secret must be set for Authorization Code Flow")

        if self._auth_settings.redirect_uri is None:
            raise ValueError("Redirect URI must be set for Authorization Code Flow")

        if self._auth_settings.scope is None:
            raise ValueError("Scope must be set for Authorization Code Flow")

        params = AuthCodeRequestParams(
            client_id=self._auth_settings.client_id,
            response_type=AUTH_CODE_FLOW_RESPONSE_TYPE,
            redirect_uri=self._auth_settings.redirect_uri,
            scope=self._auth_settings.scope,
        )
        code = await self._get_auth_code(params)

        request_body = AccessTokenRequestBody(
            grant_type=AUTH_CODE_FLOW_GRANT_TYPE,
            code=code,
            redirect_uri=self._auth_settings.redirect_uri,
        )
        auth_header = self.auth_settings.get_basic_auth()
        self._access_token_info = await self._get_access_token(request_body=request_body, auth=auth_header)

    async def refresh(self) -> None:
        """Refresh an expired access token.

        Uses the stored refresh token to obtain a new access token without requiring the user to re-authenticate.

        Returns:
            None

        Raises:
            ValueError: If `client_id` or `client_secret` is not set or an access token data is not set.
        """
        self._logger.info("Refreshing access token with Authorization Code Flow")
        self._logger.debug(f"Current auth settings: {self._auth_settings}")
        if self._auth_settings.client_id is None:
            raise ValueError("Client ID must be set for Authorization Code Flow")

        if self._auth_settings.client_secret is None:
            raise ValueError("Client Secret must be set for Authorization Code Flow")

        if self._access_token_info is None:
            raise ValueError("Access Token data is unknown!")

        if self._access_token_info.refresh_token is None:
            raise ValueError("Refresh token is unknown!")

        request_body = AccessTokenRequestBody(
            grant_type=REFRESH_AUTH_CODE_FLOW_GRANT_TYPE,
            refresh_token=self._access_token_info.refresh_token,
        )
        auth_header = self.auth_settings.get_basic_auth()
        self._access_token_info = await self._get_access_token(request_body=request_body, auth=auth_header)
