from unittest import mock

import pytest

from spotantic.endpoints.player import seek_to_position
from spotantic.models.player.requests import SeekToPositionRequest


@pytest.mark.asyncio
async def test_seek_to_position_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SeekToPositionRequest, "build", return_value=request_obj) as build_mock:
        result = await seek_to_position(client, position_ms=1234, device_id="device-1")

        build_mock.assert_called_once_with(position_ms=1234, device_id="device-1")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
