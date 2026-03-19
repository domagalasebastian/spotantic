import pytest

from spotantic.endpoints.player import get_currently_playing_track
from spotantic.models.player.requests import GetCurrentlyPlayingTrackRequest
from spotantic.models.spotify import CurrentlyPlayingItemModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.requires_active_device
async def test_get_currently_playing_track(client):
    result = await get_currently_playing_track(
        client, additional_types=[SpotifyItemType.TRACK, SpotifyItemType.EPISODE]
    )

    assert isinstance(result.request, GetCurrentlyPlayingTrackRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, CurrentlyPlayingItemModel)
