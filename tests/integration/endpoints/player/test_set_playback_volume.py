import pytest

from spotantic.endpoints.player import set_playback_volume
from spotantic.models.player.requests import SetPlaybackVolumeRequest


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_set_playback_volume(client):
    volume_percent = 100

    result = await set_playback_volume(client, volume_percent=volume_percent)

    assert isinstance(result.request, SetPlaybackVolumeRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
