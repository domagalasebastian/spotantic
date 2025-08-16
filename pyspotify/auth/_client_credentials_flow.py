from aiohttp import BasicAuth

from ._access_token_info import AccessTokenInfo
from ._auth_manager_base import AuthManagerBase
from ._auth_requests import get_access_token

CLIENT_CREDENTIALS_FLOW_GRANT_TYPE = "client_credentials"


class ClientCredentialsFlowManager(AuthManagerBase):
    async def authorize(self) -> AccessTokenInfo:
        self._logger.info("Starting Client Credentials Flow")
        self._logger.debug(f"Current auth settings: {self.auth_settings}")
        assert self.auth_settings.client_id is not None, "Client ID must be set"
        assert self.auth_settings.client_secret is not None, "Client Secret must be set"

        auth_header = BasicAuth(self.auth_settings.client_id, self.auth_settings.client_secret.get_secret_value())
        data = {
            "grant_type": CLIENT_CREDENTIALS_FLOW_GRANT_TYPE,
        }

        self._logger.info("Receiving access token from the server.")
        self._logger.debug(f"Requesting access token with data: {data}")
        token_info = await get_access_token(data=data, auth=auth_header)

        if self.auth_settings.store_access_token:
            self._logger.info(f"Saving access token to file: {self.auth_settings.access_token_file_path}")
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info
