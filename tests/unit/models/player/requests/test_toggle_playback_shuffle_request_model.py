from http import HTTPMethod

from spotantic.models.player.requests import TogglePlaybackShuffleRequest
from spotantic.models.player.requests import TogglePlaybackShuffleRequestParams
from spotantic.types import AuthScope


def test_toggle_playback_shuffle_request_model_serializes_bool_to_lowercase_string() -> None:
    req = TogglePlaybackShuffleRequest.build(state=True, device_id="device-1")

    assert req.endpoint == "me/player/shuffle"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, TogglePlaybackShuffleRequestParams)
    assert params.device_id == "device-1"

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["state"] == "true"

    req_false = TogglePlaybackShuffleRequest.build(state=False)
    params = req_false.params
    assert isinstance(params, TogglePlaybackShuffleRequestParams)
    params_false_dump = params.model_dump(by_alias=True)
    assert params_false_dump["state"] == "false"
