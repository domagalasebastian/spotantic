from pyspotify._utils.auth.generate_state import generate_hashed_state
from pyspotify._utils.auth.generate_state import generate_random_string

from .access_token_info import AccessTokenInfo
from .auth_manager_base import RefreshableAuthManager
from .auth_requests import get_access_token
from .auth_requests import get_code

AUTH_CODE_PKCE_FLOW_GRANT_TYPE = "authorization_code"
AUTH_CODE_PKCE_FLOW_RESPONSE_TYPE = "code"
AUTH_CODE_PKCE_FLOW_CODE_CHALLENGE_METHOD = "S256"
REFRESH_AUTH_CODE_PKCE_FLOW_GRANT_TYPE = "refresh_token"


class AuthCodePKCEFlowManager(RefreshableAuthManager):
    async def authorize(self) -> AccessTokenInfo:
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
        code = await get_code(redirect_uri=redirect_uri, params=params)

        data = {
            "grant_type": AUTH_CODE_PKCE_FLOW_GRANT_TYPE,
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": self.auth_settings.client_id,
            "code_verifier": code_verifier,
        }
        token_info = await get_access_token(data=data)

        if self.auth_settings.store_access_token:
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info

    async def refresh(self, refresh_token: str) -> AccessTokenInfo:
        assert self.auth_settings.client_id is not None, "Client ID must be set"

        data = {
            "grant_type": REFRESH_AUTH_CODE_PKCE_FLOW_GRANT_TYPE,
            "refresh_token": refresh_token,
            "client_id": self.auth_settings.client_id,
        }
        token_info = await get_access_token(data=data)

        if self.auth_settings.store_access_token:
            token_info.store_token(file_path=self.auth_settings.access_token_file_path)

        return token_info
