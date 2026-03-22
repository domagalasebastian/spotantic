import pytest

from spotantic.endpoints.tracks import get_several_tracks
from spotantic.models.spotify import TrackModel
from spotantic.models.tracks.requests import GetSeveralTracksRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_several_tracks(client, example_spotify_item_id):
    track_id = example_spotify_item_id[SpotifyItemType.TRACK]

    result = await get_several_tracks(client, track_ids=[track_id])

    assert isinstance(result.request, GetSeveralTracksRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
    assert len(result.data) == 1
    assert isinstance(result.data[0], TrackModel)
