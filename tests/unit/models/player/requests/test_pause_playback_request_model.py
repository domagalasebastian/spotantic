from http import HTTPMethod

from spotantic.models.player.requests import PausePlaybackRequest
from spotantic.models.player.requests import PausePlaybackRequestParams
from spotantic.types import AuthScope


def test_pause_playback_request_model():
    req = PausePlaybackRequest.build(device_id="device-1")

    assert req.endpoint == "me/player/pause"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, PausePlaybackRequestParams)
    assert params.device_id == "device-1"
    assert req.body is None
