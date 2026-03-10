from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.player.requests import SetPlaybackVolumeRequest
from spotantic.models.player.requests import SetPlaybackVolumeRequestParams
from spotantic.types import AuthScope


def test_set_playback_volume_request_model():
    req = SetPlaybackVolumeRequest.build(volume_percent=50, device_id="device-1")

    assert req.endpoint == "me/player/volume"
    assert AuthScope.USER_MODIFY_PLAYBACK_STATE in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, SetPlaybackVolumeRequestParams)
    assert params.volume_percent == 50
    assert params.device_id == "device-1"


def test_set_playback_volume_request_model_validates_volume_percent_range():
    with pytest.raises(ValidationError):
        SetPlaybackVolumeRequest.build(volume_percent=101)

    with pytest.raises(ValidationError):
        SetPlaybackVolumeRequest.build(volume_percent=-1)
