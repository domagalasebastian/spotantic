import pytest

from spotantic.endpoints.playlists import get_playlist_items
from spotantic.models.playlists.requests import GetPlaylistItemsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import PlaylistTrackModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_playlist_items(client, example_spotify_item_id):
    result = await get_playlist_items(client, playlist_id=example_spotify_item_id[SpotifyItemType.PLAYLIST], limit=50)

    assert isinstance(result.request, GetPlaylistItemsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, PlaylistTrackModel) for item in result.data.items)
