"""Unit tests for AuthManagerBase and RefreshableAuthManager classes."""

import asyncio
from datetime import datetime
from datetime import timedelta
from unittest import mock

import pytest
from pydantic import SecretStr

from spotantic.auth._auth_manager_base import AuthManagerBase
from spotantic.auth._auth_manager_base import RefreshableAuthManager
from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import AuthSettings


class ConcreteAuthManager(AuthManagerBase):
    """Concrete implementation of AuthManagerBase for testing."""

    async def authorize(self) -> None:
        """Implement abstract authorize method."""
        pass


class ConcreteRefreshableAuthManager(RefreshableAuthManager):
    """Concrete implementation of RefreshableAuthManager for testing."""

    async def authorize(self) -> None:
        """Implement abstract authorize method."""
        pass

    async def refresh(self) -> None:
        """Implement abstract refresh method."""
        pass


@pytest.fixture
def auth_settings() -> AuthSettings:
    """Fixture for AuthSettings."""
    return AuthSettings(
        client_id=SecretStr("client_id"),
        client_secret=SecretStr("secret"),
    )


@pytest.fixture
def valid_access_token_info() -> AccessTokenInfo:
    """Fixture for a valid AccessTokenInfo."""
    return AccessTokenInfo(
        access_token=SecretStr("access_token"),
        token_type="Bearer",
        expires_in=3600,
        refresh_token=SecretStr("refresh_token"),
    )


@pytest.fixture
def expired_access_token_info() -> AccessTokenInfo:
    """Fixture for an expired AccessTokenInfo."""
    token = AccessTokenInfo(
        access_token=SecretStr("access_token"),
        token_type="Bearer",
        expires_in=3600,
        refresh_token=SecretStr("refresh_token"),
    )
    # Manually set expires_at to the past
    token.expires_at = datetime.now() - timedelta(seconds=1)
    return token


class TestAuthManagerBaseProperties:
    """Tests for AuthManagerBase properties."""

    @pytest.mark.asyncio
    async def test_auth_settings_getter(self, auth_settings: AuthSettings):
        """Test that auth_settings property getter returns the settings."""
        manager = ConcreteAuthManager(auth_settings=auth_settings)

        assert manager.auth_settings == auth_settings

    @pytest.mark.asyncio
    async def test_auth_settings_setter(self, auth_settings: AuthSettings):
        """Test that auth_settings property setter updates the settings."""
        manager = ConcreteAuthManager(auth_settings=auth_settings)
        new_settings = AuthSettings(
            client_id=SecretStr("new_client_id"),
            client_secret=SecretStr("new_secret"),
        )

        manager.auth_settings = new_settings

        assert manager.auth_settings == new_settings


class TestAuthManagerBaseGetValidAccessToken:
    """Tests for AuthManagerBase.get_valid_access_token() method."""

    @pytest.mark.asyncio
    async def test_get_valid_access_token_no_token_raises_error(self, auth_settings: AuthSettings) -> None:
        """Test that get_valid_access_token raises ValueError when no token exists."""
        manager = ConcreteAuthManager(auth_settings=auth_settings, access_token_info=None)

        with pytest.raises(ValueError, match="No access token available"):
            await manager.get_valid_access_token()

    @pytest.mark.asyncio
    async def test_get_valid_access_token_returns_valid_token(
        self, auth_settings: AuthSettings, valid_access_token_info: AccessTokenInfo
    ) -> None:
        """Test that get_valid_access_token returns the token when it exists."""
        manager = ConcreteAuthManager(auth_settings=auth_settings, access_token_info=valid_access_token_info)

        token = await manager.get_valid_access_token()

        assert token == valid_access_token_info


class TestRefreshableAuthManagerGetValidAccessToken:
    """Tests for RefreshableAuthManager.get_valid_access_token() method."""

    @pytest.mark.asyncio
    async def test_get_valid_access_token_no_token_raises_error(self, auth_settings: AuthSettings) -> None:
        """Test that get_valid_access_token raises ValueError when no token exists."""
        manager = ConcreteRefreshableAuthManager(
            auth_settings=auth_settings, access_token_info=None, allow_lazy_refresh=False
        )

        with pytest.raises(ValueError, match="No access token available"):
            await manager.get_valid_access_token()

    @pytest.mark.asyncio
    async def test_get_valid_access_token_returns_valid_token_without_refresh(
        self, auth_settings: AuthSettings, valid_access_token_info: AccessTokenInfo
    ) -> None:
        """Test that get_valid_access_token returns valid token without refresh."""
        manager = ConcreteRefreshableAuthManager(
            auth_settings=auth_settings,
            access_token_info=valid_access_token_info,
            allow_lazy_refresh=False,
        )

        token = await manager.get_valid_access_token()

        assert token == valid_access_token_info

    @pytest.mark.asyncio
    async def test_get_valid_access_token_expired_logs_warning_without_lazy_refresh(
        self, auth_settings: AuthSettings, expired_access_token_info: AccessTokenInfo
    ) -> None:
        """Test that get_valid_access_token returns expired token and logs warning when lazy_refresh is False."""
        manager = ConcreteRefreshableAuthManager(
            auth_settings=auth_settings,
            access_token_info=expired_access_token_info,
            allow_lazy_refresh=False,
        )

        token = await manager.get_valid_access_token()

        # Token should be returned even though it's expired, with a warning logged
        assert token == expired_access_token_info
        assert token.is_expired() is True

    @pytest.mark.asyncio
    async def test_get_valid_access_token_expired_calls_refresh_with_lazy_refresh(
        self, auth_settings: AuthSettings, expired_access_token_info: AccessTokenInfo
    ) -> None:
        """Test that get_valid_access_token calls refresh when token is expired and lazy_refresh is True."""
        manager = ConcreteRefreshableAuthManager(
            auth_settings=auth_settings,
            access_token_info=expired_access_token_info,
            allow_lazy_refresh=True,
        )

        new_token_info = AccessTokenInfo(
            access_token=SecretStr("new_access_token"),
            token_type="Bearer",
            expires_in=3600,
            refresh_token=SecretStr("refresh_token"),
        )

        with mock.patch.object(manager, "refresh", new=mock.AsyncMock()) as mock_refresh:
            mock_refresh.side_effect = lambda: setattr(manager, "_access_token_info", new_token_info)

            token = await manager.get_valid_access_token()

            mock_refresh.assert_awaited_once()
            assert token == new_token_info
            assert manager._access_token_info == new_token_info

    @pytest.mark.asyncio
    async def test_get_valid_access_token_concurrent_refresh_with_lock(
        self, auth_settings: AuthSettings, expired_access_token_info: AccessTokenInfo
    ) -> None:
        """Test that concurrent refresh attempts are serialized with a lock."""
        manager = ConcreteRefreshableAuthManager(
            auth_settings=auth_settings,
            access_token_info=expired_access_token_info,
            allow_lazy_refresh=True,
        )

        refresh_count = 0

        async def mock_refresh_impl():
            nonlocal refresh_count
            refresh_count += 1
            await asyncio.sleep(0.1)
            # Create a new non-expired token
            manager._access_token_info = AccessTokenInfo(
                access_token=SecretStr("new_access_token"),
                token_type="Bearer",
                expires_in=3600,
                refresh_token=SecretStr("refresh_token"),
            )

        with mock.patch.object(manager, "refresh", new=mock.AsyncMock(side_effect=mock_refresh_impl)):
            # Try multiple concurrent calls to get_valid_access_token
            tasks = [manager.get_valid_access_token() for _ in range(3)]
            results = await asyncio.gather(*tasks)

            # All should return the refreshed token
            assert len(results) == 3
            # Refresh should only be called once due to the lock
            assert refresh_count == 1

    @pytest.mark.asyncio
    async def test_get_valid_access_token_no_refresh_if_not_expired_after_lock_acquire(
        self, auth_settings: AuthSettings, expired_access_token_info: AccessTokenInfo
    ) -> None:
        """Test that refresh is skipped if token is no longer expired after acquiring lock."""
        manager = ConcreteRefreshableAuthManager(
            auth_settings=auth_settings,
            access_token_info=expired_access_token_info,
            allow_lazy_refresh=True,
        )

        refresh_called = False

        async def mock_refresh_impl():
            nonlocal refresh_called
            refresh_called = True

        # Simulate another coroutine refreshing the token while waiting for the lock
        async def other_coroutine_refreshes_token():
            await asyncio.sleep(0.05)
            manager._access_token_info = AccessTokenInfo(
                access_token=SecretStr("new_access_token"),
                token_type="Bearer",
                expires_in=3600,
                refresh_token=SecretStr("refresh_token"),
            )

        with mock.patch.object(manager, "refresh", new=mock.AsyncMock(side_effect=mock_refresh_impl)):
            # Run both concurrently
            async def run_test():
                task1 = asyncio.create_task(manager.get_valid_access_token())
                task2 = asyncio.create_task(other_coroutine_refreshes_token())
                await asyncio.gather(task1, task2)

            await run_test()

            # Token should be refreshed
            assert manager._access_token_info is not None
            assert manager._access_token_info.access_token == SecretStr("new_access_token")
