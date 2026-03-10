from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.player.requests import AddItemToPlaybackQueueRequest
from spotantic.models.player.requests import AddItemToPlaybackQueueRequestParams
from spotantic.types import SpotifyTrackURI
from tests.unit._helpers import _example_instances_of_type


def test_add_item_to_playback_queue_request_model():
    example_uri = _example_instances_of_type[SpotifyTrackURI]
    req = AddItemToPlaybackQueueRequest.build(uri=example_uri, device_id="device-1")

    assert req.endpoint == "me/player/queue"
    assert req.method_type is HTTPMethod.POST

    params = req.params
    assert isinstance(params, AddItemToPlaybackQueueRequestParams)
    assert params.uri == example_uri
    assert params.device_id == "device-1"
    assert req.body is None


def test_add_item_to_playback_queue_request_model_rejects_invalid_uri() -> None:
    with pytest.raises(ValidationError):
        AddItemToPlaybackQueueRequest.build(uri="not-a-uri")
