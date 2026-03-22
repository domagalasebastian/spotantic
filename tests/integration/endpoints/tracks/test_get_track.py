import pytest

from spotantic.endpoints.tracks import get_track
from spotantic.models.spotify import TrackModel
from spotantic.models.tracks.requests import GetTrackRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_track(client, example_spotify_item_id):
    track_id = example_spotify_item_id[SpotifyItemType.TRACK]

    result = await get_track(client, track_id=track_id)

    assert isinstance(result.request, GetTrackRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, TrackModel)
