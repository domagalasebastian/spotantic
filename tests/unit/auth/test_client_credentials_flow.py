from unittest import mock

import pytest
from pydantic import SecretStr

from spotantic.auth import ClientCredentialsFlowManager
from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import AccessTokenRequestBody
from spotantic.models.auth import AuthSettings


class TestClientCredentialsFlowManagerAuthorize:
    """Tests for ClientCredentialsFlowManager.authorize() validation."""

    @pytest.mark.asyncio
    async def test_authorize_missing_client_id(self):
        """Test that authorize raises ValueError when client_id is not set."""
        settings = AuthSettings(
            client_id=None,
            client_secret=SecretStr("secret"),
        )
        manager = ClientCredentialsFlowManager(auth_settings=settings)

        with pytest.raises(ValueError, match="Client ID must be set"):
            await manager.authorize()

    @pytest.mark.asyncio
    async def test_authorize_missing_client_secret(self):
        """Test that authorize raises ValueError when client_secret is not set."""
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
            client_secret=None,
        )
        manager = ClientCredentialsFlowManager(auth_settings=settings)

        with pytest.raises(ValueError, match="Client Secret must be set"):
            await manager.authorize()

    @pytest.mark.asyncio
    async def test_authorize_missing_both_credentials(self):
        """Test that authorize raises ValueError when both client_id and client_secret are not set."""
        settings = AuthSettings(
            client_id=None,
            client_secret=None,
        )
        manager = ClientCredentialsFlowManager(auth_settings=settings)

        with pytest.raises(ValueError, match="Client ID must be set"):
            await manager.authorize()

    @pytest.mark.asyncio
    async def test_authorize_uses_basic_auth(self):
        """Test that authorize uses basic auth from settings."""
        settings = AuthSettings(
            client_id=SecretStr("client_id"),
            client_secret=SecretStr("secret"),
        )
        manager = ClientCredentialsFlowManager(auth_settings=settings)

        mock_token_info = AccessTokenInfo(
            access_token=SecretStr("access_token"),
            token_type="Bearer",
            expires_in=3600,
        )

        body = AccessTokenRequestBody(
            grant_type="client_credentials",
        )

        with mock.patch.object(
            manager, "_get_access_token", new=mock.AsyncMock(return_value=mock_token_info)
        ) as mock_get_token:
            await manager.authorize()

            mock_get_token.assert_awaited_once_with(request_body=body, auth=settings.get_basic_auth())
            assert manager._access_token_info == mock_token_info
