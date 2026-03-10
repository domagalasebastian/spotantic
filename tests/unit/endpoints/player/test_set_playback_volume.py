from unittest import mock

import pytest

from spotantic.endpoints.player import set_playback_volume
from spotantic.models.player.requests import SetPlaybackVolumeRequest


@pytest.mark.asyncio
async def test_set_playback_volume_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SetPlaybackVolumeRequest, "build", return_value=request_obj) as build_mock:
        result = await set_playback_volume(client, volume_percent=50, device_id="device-1")

        build_mock.assert_called_once_with(volume_percent=50, device_id="device-1")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
