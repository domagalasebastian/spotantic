import pytest

from spotantic.endpoints.artists import get_artist_top_tracks
from spotantic.models.artists.requests import GetArtistTopTracksRequest
from spotantic.models.spotify import TrackModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_artist_top_tracks(client, example_spotify_item_id):
    artist_id = example_spotify_item_id[SpotifyItemType.ARTIST]

    result = await get_artist_top_tracks(client, artist_id=artist_id)

    assert isinstance(result.request, GetArtistTopTracksRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
    if result.data:
        assert isinstance(result.data[0], TrackModel)
