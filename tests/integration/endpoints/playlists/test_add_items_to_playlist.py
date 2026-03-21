import pytest

from spotantic.endpoints.playlists import add_items_to_playlist
from spotantic.models.playlists.requests import AddItemsToPlaylistRequest
from spotantic.models.playlists.responses import PlaylistSnapshotResponseModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.mutation
async def test_add_items_to_playlist(client, playlist_data, example_spotify_uri):
    uris_to_add = [example_spotify_uri[SpotifyItemType.TRACK]]
    result = await add_items_to_playlist(client, playlist_id=playlist_data.playlist_id, uris=uris_to_add)

    assert isinstance(result.request, AddItemsToPlaylistRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PlaylistSnapshotResponseModel)
