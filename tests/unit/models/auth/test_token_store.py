from pathlib import Path

from pydantic import SecretStr

from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import FileTokenStore


def token_info() -> AccessTokenInfo:
    return AccessTokenInfo(
        access_token=SecretStr("access_token"),
        token_type="Bearer",
        expires_in=3600,
        refresh_token=SecretStr("refresh_token"),
    )


def test_file_token_store_round_trip(tmp_path: Path):
    """Test that FileTokenStore persists and loads token information."""
    store = FileTokenStore(tmp_path / "token.json")
    expected = token_info()

    store.save_token(expected)

    assert store.load_token() == expected


def test_file_token_store_load_missing_file(tmp_path: Path):
    """Test that a missing token file is treated as an empty store."""
    store = FileTokenStore(tmp_path / "missing-token.json")

    assert store.load_token() is None
