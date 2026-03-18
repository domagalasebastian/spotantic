import pytest

from spotantic.endpoints.artists import get_several_artists
from spotantic.models.artists.requests import GetSeveralArtistsRequest
from spotantic.models.spotify import ArtistModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_several_artists(client, example_spotify_item_id):
    artist_id = example_spotify_item_id[SpotifyItemType.ARTIST]

    result = await get_several_artists(client, artist_ids=[artist_id])

    assert isinstance(result.request, GetSeveralArtistsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
    assert len(result.data) == 1
    assert isinstance(result.data[0], ArtistModel)
