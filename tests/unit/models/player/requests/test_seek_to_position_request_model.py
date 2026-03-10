from http import HTTPMethod

from spotantic.models.player.requests import SeekToPositionRequest
from spotantic.models.player.requests import SeekToPositionRequestParams
from spotantic.types import AuthScope


def test_seek_to_position_request_model():
    req = SeekToPositionRequest.build(position_ms=1234, device_id="device-1")

    assert req.endpoint == "me/player/seek"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, SeekToPositionRequestParams)
    assert params.position_ms == 1234
    assert params.device_id == "device-1"
    assert req.body is None
