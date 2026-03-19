import pytest

from spotantic.auth import AuthCodePKCEFlowManager
from spotantic.client import SpotanticClient
from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import AuthSettings
from spotantic.types import SpotifyItemType

_example_spotify_item_id = {
    SpotifyItemType.ALBUM: "4LOrSSPct7B6yCzW1IltRd",
    SpotifyItemType.ARTIST: "250b0Wlc5Vk0CoUsaCY84M",
    SpotifyItemType.EPISODE: "1ghMJp4jwGNhX8CxDC29w9",
}

_example_spotify_uri = {
    SpotifyItemType.ALBUM: f"spotify:album:{_example_spotify_item_id[SpotifyItemType.ALBUM]}",
    SpotifyItemType.ARTIST: f"spotify:artist:{_example_spotify_item_id[SpotifyItemType.ARTIST]}",
    SpotifyItemType.EPISODE: f"spotify:episode:{_example_spotify_item_id[SpotifyItemType.EPISODE]}",
}


@pytest.fixture(scope="session")
def client() -> SpotanticClient:
    """Fixture that provides a SpotanticClient instance with an AuthCodePKCEFlowManager for authentication."""
    auth_settings = AuthSettings()
    token_info = AccessTokenInfo.load_token(auth_settings.access_token_file_path)
    auth_manager = AuthCodePKCEFlowManager(
        auth_settings=auth_settings, access_token_info=token_info, allow_lazy_refresh=True
    )

    return SpotanticClient(auth_manager=auth_manager, check_insufficient_scope=True, max_attempts=3)


@pytest.fixture
def example_spotify_item_id() -> dict[SpotifyItemType, str]:
    """Fixture that provides an example Spotify item ID for testing."""
    return _example_spotify_item_id


@pytest.fixture
def example_spotify_uri() -> dict[SpotifyItemType, str]:
    """Fixture that provides an example Spotify URI for testing."""
    return _example_spotify_uri
