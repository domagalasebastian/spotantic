from aiohttp import BasicAuth

from pyspotify._utils.auth.generate_state import generate_hashed_state
from pyspotify._utils.auth.generate_state import generate_random_string

from .access_token_info import AccessTokenInfo
from .auth_manager_base import RefreshableAuthManager
from .auth_requests import get_access_token
from .auth_requests import get_code

AUTH_CODE_FLOW_GRANT_TYPE = "authorization_code"
AUTH_CODE_FLOW_RESPONSE_TYPE = "code"
REFRESH_AUTH_CODE_FLOW_GRANT_TYPE = "refresh_token"


class AuthCodeFlowManager(RefreshableAuthManager):
    async def authorize(self) -> AccessTokenInfo:
        self._logger.info("Starting Authorization Code Flow")
        self._logger.debug(f"Current auth settings: {self.auth_settings}")
        assert self.auth_settings.client_id is not None, "Client ID must be set"
        assert self.auth_settings.client_secret is not None, "Client Secret must be set"
        assert self.auth_settings.redirect_uri is not None, "Redirect URI must be set"
        assert self.auth_settings.scope is not None, "Scope must be set"

        auth_header = BasicAuth(self.auth_settings.client_id, self.auth_settings.client_secret.get_secret_value())
        state = generate_hashed_state(generate_random_string(64))
        redirect_uri = str(self.auth_settings.redirect_uri)

        params = {
            "client_id": self.auth_settings.client_id,
            "response_type": AUTH_CODE_FLOW_RESPONSE_TYPE,
            "redirect_uri": redirect_uri,
            "scope": self.auth_settings.scope,
            "state": state,
        }
        self._logger.info(f"Receiving auth code. Website will be hosted at {redirect_uri}")
        self._logger.debug(f"Hosting Web Server with URL params: {params}")
        code = await get_code(redirect_uri=redirect_uri, params=params)

        data = {
            "grant_type": AUTH_CODE_FLOW_GRANT_TYPE,
            "code": code,
            "redirect_uri": redirect_uri,
        }
        self._logger.info("Receiving access token from the server.")
        self._logger.debug(f"Requesting access token with data: {data}")
        token_info = await get_access_token(data=data, auth=auth_header)

        if self.auth_settings.store_access_token:
            self._logger.info(f"Saving access token to file: {self.auth_settings.access_token_file_path}")
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info

    async def refresh(self, refresh_token: str) -> AccessTokenInfo:
        self._logger.info("Refreshing access token with Authorization Code Flow")
        self._logger.debug(f"Current auth settings: {self.auth_settings}")
        assert self.auth_settings.client_id is not None, "Client ID must be set"
        assert self.auth_settings.client_secret is not None, "Client Secret must be set"

        auth_header = BasicAuth(self.auth_settings.client_id, self.auth_settings.client_secret.get_secret_value())
        data = {
            "grant_type": REFRESH_AUTH_CODE_FLOW_GRANT_TYPE,
            "refresh_token": refresh_token,
        }
        self._logger.info("Receiving access token from the server.")
        self._logger.debug(f"Requesting access token with data: {data}")
        token_info = await get_access_token(data=data, auth=auth_header)

        if self.auth_settings.store_access_token:
            self._logger.info(f"Saving access token to file: {self.auth_settings.access_token_file_path}")
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info
