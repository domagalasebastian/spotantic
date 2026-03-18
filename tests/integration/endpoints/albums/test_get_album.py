import pytest

from spotantic.endpoints.albums import get_album
from spotantic.models.albums.requests import GetAlbumRequest
from spotantic.models.spotify import AlbumModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_album(client, example_spotify_item_id):
    album_id = example_spotify_item_id[SpotifyItemType.ALBUM]

    result = await get_album(client, album_id=album_id)

    assert isinstance(result.request, GetAlbumRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, AlbumModel)
