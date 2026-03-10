from unittest import mock

import pytest

from spotantic.endpoints.player import pause_playback
from spotantic.models.player.requests import PausePlaybackRequest


@pytest.mark.asyncio
async def test_pause_playback_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(PausePlaybackRequest, "build", return_value=request_obj) as build_mock:
        result = await pause_playback(client, device_id="device-1")

        build_mock.assert_called_once_with(device_id="device-1")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
