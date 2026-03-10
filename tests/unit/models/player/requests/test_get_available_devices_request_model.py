from http import HTTPMethod

from spotantic.models.player.requests import GetAvailableDevicesRequest
from spotantic.types import AuthScope


def test_get_available_devices_request_model() -> None:
    req = GetAvailableDevicesRequest.build()

    assert req.endpoint == "me/player/devices"
    assert AuthScope.USER_READ_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.GET
    assert req.params is None
    assert req.body is None
