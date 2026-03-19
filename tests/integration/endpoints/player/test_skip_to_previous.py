import pytest

from spotantic.endpoints.player import skip_to_previous
from spotantic.models.player.requests import SkipToPreviousRequest


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_skip_to_previous(client):
    result = await skip_to_previous(client)

    assert isinstance(result.request, SkipToPreviousRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
