import pytest

from spotantic.endpoints.player import get_user_queue
from spotantic.models.player.requests import GetUserQueueRequest
from spotantic.models.player.responses import GetUserQueueResponse


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_user_queue(client):
    result = await get_user_queue(client)

    assert isinstance(result.request, GetUserQueueRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, GetUserQueueResponse)
