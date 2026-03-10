from http import HTTPMethod

from spotantic.models.player.requests import SkipToNextRequest
from spotantic.models.player.requests import SkipToNextRequestParams
from spotantic.types import AuthScope


def test_skip_to_next_request_model():
    req = SkipToNextRequest.build(device_id="device-1")

    assert req.endpoint == "me/player/next"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.POST

    params = req.params
    assert isinstance(params, SkipToNextRequestParams)
    assert params.device_id == "device-1"
    assert req.body is None
