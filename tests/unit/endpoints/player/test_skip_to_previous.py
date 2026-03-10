from unittest import mock

import pytest

from spotantic.endpoints.player import skip_to_previous
from spotantic.models.player.requests import SkipToPreviousRequest


@pytest.mark.asyncio
async def test_skip_to_previous_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SkipToPreviousRequest, "build", return_value=request_obj) as build_mock:
        result = await skip_to_previous(client, device_id="device-1")

        build_mock.assert_called_once_with(device_id="device-1")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
