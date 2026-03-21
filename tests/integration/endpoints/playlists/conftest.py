import pytest

from spotantic.endpoints.playlists import add_items_to_playlist
from spotantic.types import SpotifyItemType


@pytest.fixture
async def non_empty_playlist_data(client, playlist_data, example_spotify_uri):
    """Fixture that ensures the test playlist has at least one track."""
    track_uri = example_spotify_uri[SpotifyItemType.TRACK]
    await add_items_to_playlist(client, playlist_id=playlist_data.playlist_id, uris=[track_uri])

    return playlist_data, track_uri
