import pytest

from spotantic.endpoints.player import toggle_playback_shuffle
from spotantic.models.player.requests import TogglePlaybackShuffleRequest


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_toggle_playback_shuffle(client):
    for state in (True, False):
        result = await toggle_playback_shuffle(client, state=state)

        assert isinstance(result.request, TogglePlaybackShuffleRequest)
        assert result.response is None or isinstance(result.response, bytes)
        assert result.data is None
