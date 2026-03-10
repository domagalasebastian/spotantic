from unittest import mock

import pytest

from spotantic.endpoints.player import skip_to_next
from spotantic.models.player.requests import SkipToNextRequest


@pytest.mark.asyncio
async def test_skip_to_next_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SkipToNextRequest, "build", return_value=request_obj) as build_mock:
        result = await skip_to_next(client, device_id="device-1")

        build_mock.assert_called_once_with(device_id="device-1")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
