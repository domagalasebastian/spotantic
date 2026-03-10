from http import HTTPMethod

from spotantic.models.player.requests import SetRepeatModeRequest
from spotantic.models.player.requests import SetRepeatModeRequestParams
from spotantic.types import AuthScope
from spotantic.types import RepeatMode


def test_set_repeat_mode_request_model_serializes_enum_value() -> None:
    req = SetRepeatModeRequest.build(state=RepeatMode.TRACK, device_id="device-1")

    assert req.endpoint == "me/player/repeat"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, SetRepeatModeRequestParams)
    assert params.state == RepeatMode.TRACK
    assert params.device_id == "device-1"

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["state"] == "track"
