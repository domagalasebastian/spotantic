import pytest

from spotantic.endpoints.artists import get_artist
from spotantic.models.artists.requests import GetArtistRequest
from spotantic.models.spotify import ArtistModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_artist(client, example_spotify_item_id):
    artist_id = example_spotify_item_id[SpotifyItemType.ARTIST]

    result = await get_artist(client, artist_id=artist_id)

    assert isinstance(result.request, GetArtistRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, ArtistModel)
