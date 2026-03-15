from unittest import mock

import pytest
from pydantic import HttpUrl
from pydantic import SecretStr

from spotantic.auth import AuthCodePKCEFlowManager
from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import AccessTokenRequestBody
from spotantic.models.auth import AuthCodeRequestParams
from spotantic.models.auth import AuthSettings


class TestAuthCodePKCEFlowManagerAuthorize:
    """Tests for AuthCodePKCEFlowManager.authorize() validation."""

    @pytest.mark.asyncio
    async def test_authorize_missing_client_id(self):
        """Test that authorize raises ValueError when client_id is not set."""
        settings = AuthSettings(
            client_id=None,
            redirect_uri=HttpUrl("http://localhost:8000/callback"),
            scope="user-read-private",
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings)

        with pytest.raises(ValueError, match="Client ID must be set"):
            await manager.authorize()

    @pytest.mark.asyncio
    async def test_authorize_missing_redirect_uri(self):
        """Test that authorize raises ValueError when redirect_uri is not set."""
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
            redirect_uri=None,
            scope="user-read-private",
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings)

        with pytest.raises(ValueError, match="Redirect URI must be set"):
            await manager.authorize()

    @pytest.mark.asyncio
    async def test_authorize_missing_scope(self):
        """Test that authorize raises ValueError when scope is not set."""
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
            redirect_uri=HttpUrl("http://localhost:8000/callback"),
            scope=None,
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings)

        with pytest.raises(ValueError, match="Scope must be set"):
            await manager.authorize()

    @pytest.mark.asyncio
    async def test_authorize_calls_get_access_token_with_authorization_code_grant(self):
        """Test that authorize calls _get_access_token with authorization_code grant type."""
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
            redirect_uri=HttpUrl("http://localhost:8000/callback"),
            scope="user-read-private",
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings)

        mock_token_info = AccessTokenInfo(
            access_token=SecretStr("access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=SecretStr("refresh_token"),
        )

        params = AuthCodeRequestParams(
            client_id=SecretStr("client_id"),
            response_type="code",
            redirect_uri=HttpUrl("http://localhost:8000/callback"),
            scope="user-read-private",
            code_challenge_method="S256",
            code_challenge="code_challenge_123",
        )

        body = AccessTokenRequestBody(
            grant_type="authorization_code",
            code="auth_code_123",
            redirect_uri=HttpUrl("http://localhost:8000/callback"),
            client_id=SecretStr("client_id"),
            code_verifier="code_verifier_123",
        )

        with (
            mock.patch.object(
                manager, "_get_auth_code", new=mock.AsyncMock(return_value="auth_code_123")
            ) as mock_get_code,
            mock.patch.object(
                manager, "_get_access_token", new=mock.AsyncMock(return_value=mock_token_info)
            ) as mock_get_token,
            mock.patch(
                "spotantic.auth._auth_code_pkce_flow.generate_pkce_code_verifier", return_value="code_verifier_123"
            ),
            mock.patch(
                "spotantic.auth._auth_code_pkce_flow.get_pkce_code_challenge", return_value="code_challenge_123"
            ),
        ):
            await manager.authorize()

            mock_get_code.assert_awaited_once_with(params)
            mock_get_token.assert_awaited_once_with(request_body=body)
            assert manager._access_token_info == mock_token_info


class TestAuthCodePKCEFlowManagerRefresh:
    """Tests for AuthCodePKCEFlowManager.refresh() validation."""

    @pytest.mark.asyncio
    async def test_refresh_missing_client_id(self):
        """Test that refresh raises ValueError when client_id is not set."""
        settings = AuthSettings(
            client_id=None,
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings)

        with pytest.raises(ValueError, match="Client ID must be set"):
            await manager.refresh()

    @pytest.mark.asyncio
    async def test_refresh_missing_access_token_info(self):
        """Test that refresh raises ValueError when access_token_info is not set."""
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings, access_token_info=None)

        with pytest.raises(ValueError, match="Access Token data is unknown"):
            await manager.refresh()

    @pytest.mark.asyncio
    async def test_refresh_missing_refresh_token(self):
        """Test that refresh raises ValueError when refresh_token is not set."""
        token_info = AccessTokenInfo(
            access_token=SecretStr("access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=None,
        )
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings, access_token_info=token_info)

        with pytest.raises(ValueError, match="Refresh token is unknown"):
            await manager.refresh()

    @pytest.mark.asyncio
    async def test_refresh_calls_get_access_token_with_refresh_token_grant(self):
        """Test that refresh calls _get_access_token with refresh_token grant type."""
        token_info = AccessTokenInfo(
            access_token=SecretStr("access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=SecretStr("refresh_token"),
        )
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
        )
        manager = AuthCodePKCEFlowManager(auth_settings=settings, access_token_info=token_info)

        new_token_info = AccessTokenInfo(
            access_token=SecretStr("new_access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=SecretStr("new_refresh_token"),
        )

        body = AccessTokenRequestBody(
            grant_type="refresh_token",
            refresh_token=SecretStr("refresh_token"),
            client_id=SecretStr("client_id"),
        )

        with mock.patch.object(
            manager, "_get_access_token", new=mock.AsyncMock(return_value=new_token_info)
        ) as mock_get_token:
            await manager.refresh()

            mock_get_token.assert_awaited_once_with(request_body=body)
            assert manager._access_token_info == new_token_info
