import pytest

from spotantic.endpoints.albums import get_album_tracks
from spotantic.models.albums.requests import GetAlbumTracksRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedTrackModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_album_tracks(client, example_spotify_item_id):
    album_id = example_spotify_item_id[SpotifyItemType.ALBUM]

    result = await get_album_tracks(client, album_id=album_id, limit=50)

    assert isinstance(result.request, GetAlbumTracksRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, SimplifiedTrackModel) for item in result.data.items)
