from datetime import datetime
from datetime import timedelta

from pydantic import SecretStr

from spotantic.models.auth import AccessTokenInfo


def test_access_token_info_valid():
    """Test valid AccessTokenInfo initialization."""
    before = datetime.now()
    token_info = AccessTokenInfo(
        access_token=SecretStr("test_access_token"),
        token_type="Bearer",
        expires_in=3600,
    )
    after = datetime.now()

    assert token_info.access_token.get_secret_value() == "test_access_token"
    assert token_info.token_type == "Bearer"
    assert token_info.scope is None
    assert token_info.expires_in == 3600
    assert token_info.refresh_token is None
    # expires_at is automatically set based on expires_in
    assert token_info.expires_at is not None
    assert before + timedelta(seconds=3600) <= token_info.expires_at <= after + timedelta(seconds=3600)


def test_access_token_info_with_all_fields():
    """Test AccessTokenInfo with all fields populated."""
    expires_at = datetime.now() + timedelta(hours=1)
    token_info = AccessTokenInfo(
        access_token=SecretStr("test_access_token"),
        token_type="Bearer",
        scope="user-read-private user-read-email",
        expires_in=3600,
        refresh_token=SecretStr("test_refresh_token"),
        expires_at=expires_at,
    )

    assert token_info.access_token.get_secret_value() == "test_access_token"
    assert token_info.token_type == "Bearer"
    assert token_info.scope == "user-read-private user-read-email"
    assert token_info.expires_in == 3600
    assert token_info.refresh_token is not None
    assert token_info.refresh_token.get_secret_value() == "test_refresh_token"
    assert token_info.expires_at == expires_at


def test_access_token_info_serialization():
    """Test AccessTokenInfo serialization to dict."""
    token_info = AccessTokenInfo(
        access_token=SecretStr("test_access_token"),
        token_type="Bearer",
        scope="user-read-private",
        expires_in=3600,
        refresh_token=SecretStr("test_refresh_token"),
    )

    data = token_info.model_dump(by_alias=True, mode="json")
    assert data["access_token"] == "test_access_token"
    assert data["token_type"] == "Bearer"
    assert data["scope"] == "user-read-private"
    assert data["expires_in"] == 3600
    assert data["refresh_token"] == "test_refresh_token"
