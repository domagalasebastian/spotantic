from unittest import mock

import pytest
from pydantic import ValidationError

from spotantic.endpoints.markets import get_available_markets
from spotantic.models.markets.requests import GetAvailableMarketsRequest


@pytest.mark.asyncio
async def test_get_available_markets_builds_request_and_returns_list_of_markets():
    client = mock.AsyncMock()
    fake_response = ["US", "CA"]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(GetAvailableMarketsRequest, "build", return_value=request_obj) as build_mock:
        result = await get_available_markets(client)

        build_mock.assert_called_once_with()
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data == fake_response


@pytest.mark.asyncio
async def test_get_available_markets_raises_on_invalid_response_type():
    client = mock.AsyncMock()
    # Response must be list[str] matching SpotifyMarketID (2-letter codes)
    client.request_json.return_value = {"US": True}

    with mock.patch.object(GetAvailableMarketsRequest, "build", return_value=object()):
        with pytest.raises(ValidationError):
            await get_available_markets(client)
