from pyspotify._utils.auth import generate_pkce_code_verifier
from pyspotify._utils.auth import get_pkce_code_challenge
from pyspotify.models.auth import AccessTokenRequestBody
from pyspotify.models.auth import AuthCodeRequestParams

from ._auth_manager_base import RefreshableAuthManager

AUTH_CODE_PKCE_FLOW_GRANT_TYPE = "authorization_code"
AUTH_CODE_PKCE_FLOW_RESPONSE_TYPE = "code"
AUTH_CODE_PKCE_FLOW_CODE_CHALLENGE_METHOD = "S256"
REFRESH_AUTH_CODE_PKCE_FLOW_GRANT_TYPE = "refresh_token"


class AuthCodePKCEFlowManager(RefreshableAuthManager):
    """Manager for Spotify OAuth2 Authorization Code Flow with PKCE.

    The Authorization Code Flow with PKCE (Proof Key for Code Exchange) is designed for
    public clients such as mobile and single-page applications where the client secret
    cannot be securely stored.

    PKCE adds an extra layer of security by using dynamically generated code verifiers
    and challenges instead of relying on a static client secret. For more information refer to:
    `Authorization Code with PKCE Flow
    <https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow>`_.
    """

    async def authorize(self) -> None:
        """Authorize using the Authorization Code Flow with PKCE.

        Initiates the authorization process by:
        1. Generating a code verifier and challenge
        2. Redirecting the user to Spotify's authorization endpoint
        3. Exchanging the authorization code for an access token

        Returns:
            None

        Raises:
            ValueError: If any required settings (`client_id`, `redirect_uri`, `scope`) are not set.
        """
        self._logger.info("Starting Authorization Code PKCE Flow")
        self._logger.debug(f"Current auth settings: {self._auth_settings}")
        if self._auth_settings.client_id is None:
            raise ValueError("Client ID must be set for Authorization Code PKCE Flow")

        if self._auth_settings.redirect_uri is None:
            raise ValueError("Redirect URI must be set for Authorization Code PKCE Flow")

        if self._auth_settings.scope is None:
            raise ValueError("Scope must be set for Authorization Code PKCE Flow")

        code_verifier = generate_pkce_code_verifier(64)
        code_challenge = get_pkce_code_challenge(code_verifier)
        params = AuthCodeRequestParams(
            client_id=self._auth_settings.client_id,
            response_type=AUTH_CODE_PKCE_FLOW_RESPONSE_TYPE,
            redirect_uri=self._auth_settings.redirect_uri,
            scope=self._auth_settings.scope,
            code_challenge_method=AUTH_CODE_PKCE_FLOW_CODE_CHALLENGE_METHOD,
            code_challenge=code_challenge,
        )
        code = await self._get_auth_code(params)

        request_body = AccessTokenRequestBody(
            grant_type=AUTH_CODE_PKCE_FLOW_GRANT_TYPE,
            code=code,
            redirect_uri=self._auth_settings.redirect_uri,
            client_id=self._auth_settings.client_id,
            code_verifier=code_verifier,
        )
        self._access_token_info = await self._get_access_token(request_body=request_body)

    async def refresh(self) -> None:
        """Refresh an expired access token.

        Uses the stored refresh token to obtain a new access token without requiring
        the user to re-authenticate.

        Returns:
            None

        Raises:
            ValueError: If ``client_id`` or an access token data is not set.
        """
        self._logger.info("Refreshing access token with Authorization Code PKCE Flow")
        self._logger.debug(f"Current auth settings: {self._auth_settings}")

        if self._auth_settings.client_id is None:
            raise ValueError("Client ID must be set for Authorization Code PKCE Flow")

        if self._access_token_info is None:
            raise ValueError("Access Token data is unknown!")

        if self._access_token_info.refresh_token is None:
            raise ValueError("Refresh token is unknown!")

        request_body = AccessTokenRequestBody(
            grant_type=REFRESH_AUTH_CODE_PKCE_FLOW_GRANT_TYPE,
            refresh_token=self._access_token_info.refresh_token,
            client_id=self._auth_settings.client_id,
        )
        self._access_token_info = await self._get_access_token(request_body=request_body)
