import pytest

from spotantic.endpoints.player import skip_to_next
from spotantic.models.player.requests import SkipToNextRequest


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_skip_to_next(client):
    result = await skip_to_next(client)

    assert isinstance(result.request, SkipToNextRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
