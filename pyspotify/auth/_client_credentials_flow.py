from aiohttp import BasicAuth

from pyspotify.models.auth import AccessTokenInfo
from pyspotify.models.auth import AccessTokenRequestBody

from ._auth_manager_base import AuthManagerBase

CLIENT_CREDENTIALS_FLOW_GRANT_TYPE = "client_credentials"


class ClientCredentialsFlowManager(AuthManagerBase):
    """Manager for Spotify OAuth2 Client Credentials Flow.

    The Client Credentials Flow is used by applications that need access to
    protected resources without user interaction. This flow is suitable for
    server-to-server interactions where user authentication is not required.
    For more information refer to:
    `Client Credentials Flow <https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow>`_.
    """

    async def authorize(self) -> AccessTokenInfo:
        """Authorize using the Client Credentials Flow.

        Retrieves an access token using the application's client ID and client secret.
        The access token can be used to make authenticated requests to the Spotify API.

        Returns:
            Object containing the access token and its metadata.

        Raises:
            ValueError: If `client_id` or `client_secret` is not set.
        """
        self._logger.info("Starting Client Credentials Flow")
        self._logger.debug(f"Current auth settings: {self.auth_settings}")
        if self.auth_settings.client_id is None:
            raise ValueError("Client ID must be set for Client Credentials Flow")

        if self.auth_settings.client_secret is None:
            raise ValueError("Client Secret must be set for Client Credentials Flow")

        request_body = AccessTokenRequestBody(
            grant_type=CLIENT_CREDENTIALS_FLOW_GRANT_TYPE,
        )
        auth_header = BasicAuth(self.auth_settings.client_id, self.auth_settings.client_secret.get_secret_value())
        token_info = await self.get_access_token(request_body=request_body, auth=auth_header)

        return token_info
