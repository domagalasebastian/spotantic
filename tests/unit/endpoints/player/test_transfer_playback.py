from unittest import mock

import pytest

from spotantic.endpoints.player import transfer_playback
from spotantic.models.player.requests import TransferPlaybackRequest


@pytest.mark.asyncio
async def test_transfer_playback_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(TransferPlaybackRequest, "build", return_value=request_obj) as build_mock:
        result = await transfer_playback(client, device_ids=["d1"], play=True)

        build_mock.assert_called_once_with(device_ids=["d1"], play=True)
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
