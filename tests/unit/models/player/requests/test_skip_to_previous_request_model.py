from http import HTTPMethod

from spotantic.models.player.requests import SkipToPreviousRequest
from spotantic.models.player.requests import SkipToPreviousRequestParams
from spotantic.types import AuthScope


def test_skip_to_previous_request_model():
    req = SkipToPreviousRequest.build(device_id="device-1")

    assert req.endpoint == "me/player/previous"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.POST

    params = req.params
    assert isinstance(params, SkipToPreviousRequestParams)
    assert params.device_id == "device-1"
    assert req.body is None
