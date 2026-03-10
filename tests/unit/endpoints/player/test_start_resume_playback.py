from unittest import mock

import pytest

from spotantic.endpoints.player import start_resume_playback
from spotantic.models.player.requests import StartResumePlaybackRequest


@pytest.mark.asyncio
async def test_start_resume_playback_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(StartResumePlaybackRequest, "build", return_value=request_obj) as build_mock:
        result = await start_resume_playback(
            client,
            device_id="device-1",
            context_uri="spotify:album:AaBbCcDdEeFfGgHhIiJjKk",
            position_ms=1000,
        )

        build_mock.assert_called_once_with(
            device_id="device-1",
            context_uri="spotify:album:AaBbCcDdEeFfGgHhIiJjKk",
            uris=None,
            offset=None,
            position_ms=1000,
        )
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
