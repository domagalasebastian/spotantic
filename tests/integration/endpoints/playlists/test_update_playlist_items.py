import pytest

from spotantic.endpoints.playlists import update_playlist_items
from spotantic.models.playlists.requests import UpdatePlaylistItemsRequest
from spotantic.models.playlists.responses import PlaylistSnapshotResponseModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.mutation
async def test_update_playlist_items(client, non_empty_playlist_data, example_spotify_uri):
    playlist, _ = non_empty_playlist_data
    new_uri = example_spotify_uri[SpotifyItemType.EPISODE]

    result = await update_playlist_items(
        client, playlist_id=playlist.playlist_id, uris=[new_uri], range_start=0, insert_before=0
    )

    assert isinstance(result.request, UpdatePlaylistItemsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PlaylistSnapshotResponseModel)  # The Spotify API returns an empty object on success
