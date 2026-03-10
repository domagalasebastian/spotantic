from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.player.requests import TransferPlaybackRequest
from spotantic.models.player.requests import TransferPlaybackRequestBody
from spotantic.types import AuthScope


def test_transfer_playback_request_model_sets_json_content_type_and_body() -> None:
    req = TransferPlaybackRequest.build(device_ids=["d1"], play=True)

    assert req.endpoint == "me/player"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.PUT
    assert req.headers.content_type == "application/json"

    body = req.body
    assert isinstance(body, TransferPlaybackRequestBody)
    assert body.device_ids == ["d1"]
    assert body.play is True


def test_transfer_playback_request_model_rejects_too_many_devices() -> None:
    with pytest.raises(ValidationError):
        TransferPlaybackRequest.build(device_ids=["d1", "d2"])
