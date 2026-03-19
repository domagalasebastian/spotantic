import pytest

from spotantic.endpoints.player import seek_to_position
from spotantic.models.player.requests import SeekToPositionRequest


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_seek_to_position(client):
    position_ms = 0

    result = await seek_to_position(client, position_ms=position_ms)

    assert isinstance(result.request, SeekToPositionRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
