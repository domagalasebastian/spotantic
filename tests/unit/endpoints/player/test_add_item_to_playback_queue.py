from unittest import mock

import pytest

from spotantic.endpoints.player import add_item_to_playback_queue
from spotantic.models.player.requests import AddItemToPlaybackQueueRequest
from spotantic.types import SpotifyTrackURI


@pytest.mark.asyncio
async def test_add_item_to_playback_queue_builds_request_and_returns_none_data(example_instances_of_type):
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()
    example_uri = example_instances_of_type[SpotifyTrackURI]

    with mock.patch.object(AddItemToPlaybackQueueRequest, "build", return_value=request_obj) as build_mock:
        result = await add_item_to_playback_queue(client, uri=example_uri, device_id="device-1")

        build_mock.assert_called_once_with(uri=example_uri, device_id="device-1")
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
