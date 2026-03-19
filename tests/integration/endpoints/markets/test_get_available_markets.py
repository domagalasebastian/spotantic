import pytest

from spotantic.endpoints.markets import get_available_markets
from spotantic.models.markets.requests import GetAvailableMarketsRequest


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_available_markets(client):
    result = await get_available_markets(client)

    assert isinstance(result.request, GetAvailableMarketsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
