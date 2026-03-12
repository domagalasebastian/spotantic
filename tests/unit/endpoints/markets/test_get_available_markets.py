from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.markets import get_available_markets
from spotantic.models.markets.requests import GetAvailableMarketsRequest


@pytest.mark.asyncio
async def test_get_available_markets_builds_request_and_returns_list_of_markets():
    client = mock.AsyncMock()
    fake_response = {"markets": ["US", "CA"]}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(markets=["US", "CA"])

    with mock.patch.object(GetAvailableMarketsRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.markets.responses.GetAvailableMarketsResponse.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await get_available_markets(client)

            build_mock.assert_called_once_with()
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data == fake_model.markets
