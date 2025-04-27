from aiohttp import BasicAuth

from .access_token_info import AccessTokenInfo
from .auth_manager_base import AuthManagerBase
from .auth_requests import get_access_token

CLIENT_CREDENTIALS_FLOW_GRANT_TYPE = "client_credentials"


class ClientCredentialsFlowManager(AuthManagerBase):
    async def authorize(self) -> AccessTokenInfo:
        assert self.auth_settings.client_id is not None, "Client ID must be set"
        assert self.auth_settings.client_secret is not None, "Client Secret must be set"

        auth_header = BasicAuth(self.auth_settings.client_id, self.auth_settings.client_secret)
        data = {
            "grant_type": CLIENT_CREDENTIALS_FLOW_GRANT_TYPE,
        }

        token_info = await get_access_token(data=data, auth=auth_header)

        if self.auth_settings.store_access_token:
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info
