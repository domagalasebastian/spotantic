from pyspotify._utils.auth.generate_state import generate_hashed_state
from pyspotify._utils.auth.generate_state import generate_random_string

from ._access_token_info import AccessTokenInfo
from ._auth_manager_base import RefreshableAuthManager
from ._auth_requests import get_access_token
from ._auth_requests import get_code

AUTH_CODE_PKCE_FLOW_GRANT_TYPE = "authorization_code"
AUTH_CODE_PKCE_FLOW_RESPONSE_TYPE = "code"
AUTH_CODE_PKCE_FLOW_CODE_CHALLENGE_METHOD = "S256"
REFRESH_AUTH_CODE_PKCE_FLOW_GRANT_TYPE = "refresh_token"


class AuthCodePKCEFlowManager(RefreshableAuthManager):
    async def authorize(self) -> AccessTokenInfo:
        self._logger.info("Starting Authorization Code PKCE Flow")
        self._logger.debug(f"Current auth settings: {self.auth_settings}")
        assert self.auth_settings.client_id is not None, "Client ID must be set"
        assert self.auth_settings.redirect_uri is not None, "Redirect URI must be set"
        assert self.auth_settings.scope is not None, "Scope must be set"

        state = generate_hashed_state(generate_random_string(64))
        redirect_uri = str(self.auth_settings.redirect_uri)

        code_verifier = generate_random_string(64)
        code_challenge = generate_hashed_state(code_verifier)
        params = {
            "client_id": self.auth_settings.client_id,
            "response_type": AUTH_CODE_PKCE_FLOW_RESPONSE_TYPE,
            "redirect_uri": redirect_uri,
            "scope": self.auth_settings.scope,
            "state": state,
            "code_challenge_method": AUTH_CODE_PKCE_FLOW_CODE_CHALLENGE_METHOD,
            "code_challenge": code_challenge,
        }
        self._logger.info(f"Receiving auth code. Website will be hosted at {redirect_uri}")
        self._logger.debug(f"Hosting Web Server with URL params: {params}")
        code = await get_code(redirect_uri=redirect_uri, params=params)

        data = {
            "grant_type": AUTH_CODE_PKCE_FLOW_GRANT_TYPE,
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": self.auth_settings.client_id,
            "code_verifier": code_verifier,
        }
        self._logger.info("Receiving access token from the server.")
        self._logger.debug(f"Requesting access token with data: {data}")
        token_info = await get_access_token(data=data)

        if self.auth_settings.store_access_token:
            self._logger.info(f"Saving access token to file: {self.auth_settings.access_token_file_path}")
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info

    async def refresh(self, refresh_token: str) -> AccessTokenInfo:
        assert self.auth_settings.client_id is not None, "Client ID must be set"
        self._logger.info("Refreshing access token with Authorization Code PKCE Flow")
        self._logger.debug(f"Current auth settings: {self.auth_settings}")

        data = {
            "grant_type": REFRESH_AUTH_CODE_PKCE_FLOW_GRANT_TYPE,
            "refresh_token": refresh_token,
            "client_id": self.auth_settings.client_id,
        }
        self._logger.info("Receiving access token from the server.")
        self._logger.debug(f"Requesting access token with data: {data}")
        token_info = await get_access_token(data=data)

        if self.auth_settings.store_access_token:
            self._logger.info(f"Saving access token to file: {self.auth_settings.access_token_file_path}")
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info
