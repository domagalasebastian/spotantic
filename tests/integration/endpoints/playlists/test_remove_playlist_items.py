import pytest

from spotantic.endpoints.playlists import remove_playlist_items
from spotantic.models.playlists.requests import RemovePlaylistItemsRequest
from spotantic.models.playlists.responses import PlaylistSnapshotResponseModel


@pytest.mark.asyncio
@pytest.mark.mutation
async def test_remove_playlist_items(client, non_empty_playlist_data):
    playlist, track_uri = non_empty_playlist_data
    result = await remove_playlist_items(client, playlist_id=playlist.playlist_id, uris=[track_uri])

    assert isinstance(result.request, RemovePlaylistItemsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PlaylistSnapshotResponseModel)
