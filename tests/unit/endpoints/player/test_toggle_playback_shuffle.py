from unittest import mock

import pytest

from spotantic.endpoints.player import toggle_playback_shuffle
from spotantic.models.player.requests import TogglePlaybackShuffleRequest


@pytest.mark.asyncio
async def test_toggle_playback_shuffle_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(TogglePlaybackShuffleRequest, "build", return_value=request_obj) as build_mock:
        result = await toggle_playback_shuffle(client, state=True, device_id="device-1")

        build_mock.assert_called_once_with(state=True, device_id="device-1")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
