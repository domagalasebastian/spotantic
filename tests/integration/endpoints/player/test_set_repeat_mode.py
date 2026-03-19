import pytest

from spotantic.endpoints.player import set_repeat_mode
from spotantic.models.player.requests import SetRepeatModeRequest
from spotantic.types import RepeatMode


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_set_repeat_mode(client):
    repeat_mode = RepeatMode.TRACK

    result = await set_repeat_mode(client, state=repeat_mode)

    assert isinstance(result.request, SetRepeatModeRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
