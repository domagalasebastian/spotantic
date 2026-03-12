from pathlib import Path

import pytest
from aiohttp import BasicAuth
from pydantic import HttpUrl
from pydantic import SecretStr

from spotantic.models.auth import AuthSettings


def test_auth_settings_with_all_fields():
    """Test AuthSettings with all fields provided."""
    settings = AuthSettings(
        client_id=SecretStr("test_client_id_123"),
        client_secret=SecretStr("test_client_secret_123"),
        redirect_uri=HttpUrl("http://localhost:8000/callback"),
        scope="user-read-private user-read-email",
        store_access_token=True,
        access_token_file_path=Path("./token_cache"),
    )

    assert settings.client_id is not None
    assert settings.client_secret is not None
    assert settings.client_id.get_secret_value() == "test_client_id_123"
    assert settings.client_secret.get_secret_value() == "test_client_secret_123"
    assert settings.redirect_uri == HttpUrl("http://localhost:8000/callback")
    assert settings.scope == "user-read-private user-read-email"
    assert settings.store_access_token is True
    assert settings.access_token_file_path == Path("./token_cache")


def test_auth_settings_get_basic_auth_success():
    """Test get_basic_auth with valid client_id and client_secret."""
    settings = AuthSettings(
        client_id=SecretStr("test_client_id_123"),
        client_secret=SecretStr("test_client_secret_123"),
    )

    basic_auth = settings.get_basic_auth()
    assert isinstance(basic_auth, BasicAuth)
    assert basic_auth.login == "test_client_id_123"
    assert basic_auth.password == "test_client_secret_123"


def test_auth_settings_get_basic_auth_missing_client_id():
    """Test get_basic_auth without client_id raises ValueError."""
    settings = AuthSettings(
        client_secret=SecretStr("test_client_secret_123"),
        client_id=None,
    )

    with pytest.raises(ValueError):
        settings.get_basic_auth()


def test_auth_settings_get_basic_auth_missing_client_secret():
    """Test get_basic_auth without client_secret raises ValueError."""
    settings = AuthSettings(
        client_id=SecretStr("test_client_id_123"),
        client_secret=None,
    )

    with pytest.raises(ValueError):
        settings.get_basic_auth()


def test_auth_settings_get_basic_auth_missing_both():
    """Test get_basic_auth without both client_id and client_secret raises ValueError."""
    settings = AuthSettings(
        client_id=None,
        client_secret=None,
    )

    with pytest.raises(ValueError):
        settings.get_basic_auth()


def test_auth_settings_custom_access_token_file_path():
    """Test AuthSettings with custom access_token_file_path."""
    custom_path = Path("./custom_token_cache")
    settings = AuthSettings(
        access_token_file_path=custom_path,
    )

    assert settings.access_token_file_path == custom_path


def test_auth_settings_store_access_token_flag():
    """Test AuthSettings store_access_token flag."""
    settings_false = AuthSettings(store_access_token=False)
    assert settings_false.store_access_token is False

    settings_true = AuthSettings(store_access_token=True)
    assert settings_true.store_access_token is True
