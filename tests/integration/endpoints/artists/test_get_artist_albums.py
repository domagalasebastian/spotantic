import pytest

from spotantic.endpoints.artists import get_artist_albums
from spotantic.models.artists.requests import GetArtistAlbumsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedAlbumModel
from spotantic.types import AlbumTypes
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_artist_albums(client, example_spotify_item_id):
    artist_id = example_spotify_item_id[SpotifyItemType.ARTIST]

    result = await get_artist_albums(client, artist_id=artist_id, limit=50, include_groups=[AlbumTypes.ALBUM])

    assert isinstance(result.request, GetArtistAlbumsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    if result.data.items:
        assert isinstance(result.data.items[0], SimplifiedAlbumModel)
