import pytest

from spotantic.endpoints.albums import get_several_albums
from spotantic.models.albums.requests import GetSeveralAlbumsRequest
from spotantic.models.spotify import AlbumModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_several_albums(client, example_spotify_item_id):
    album_id = example_spotify_item_id[SpotifyItemType.ALBUM]

    result = await get_several_albums(client, album_ids=[album_id])

    assert isinstance(result.request, GetSeveralAlbumsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
    assert len(result.data) == 1
    assert isinstance(result.data[0], AlbumModel)
