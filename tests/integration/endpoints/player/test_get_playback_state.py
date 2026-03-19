import pytest

from spotantic.endpoints.player import get_playback_state
from spotantic.models.player.requests import GetPlaybackStateRequest
from spotantic.models.spotify import PlaybackStateModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.requires_active_device
async def test_get_playback_state(client):
    result = await get_playback_state(client, additional_types=[SpotifyItemType.TRACK, SpotifyItemType.EPISODE])

    assert isinstance(result.request, GetPlaybackStateRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PlaybackStateModel)
