from http import HTTPMethod

import pytest

from spotantic.models.player.requests import GetCurrentlyPlayingTrackRequest
from spotantic.models.player.requests import GetCurrentlyPlayingTrackRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemType


def test_get_currently_playing_track_request_model_serializes_additional_types() -> None:
    req = GetCurrentlyPlayingTrackRequest.build(
        additional_types=[SpotifyItemType.TRACK, SpotifyItemType.EPISODE], market="US"
    )

    assert req.endpoint == "me/player/currently-playing"
    assert AuthScope.USER_READ_CURRENTLY_PLAYING in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetCurrentlyPlayingTrackRequestParams)
    assert params.market == "US"

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["additional_types"] == "track,episode"


def test_get_currently_playing_track_request_model_rejects_unsupported_item_type() -> None:
    with pytest.raises(ValueError):
        GetCurrentlyPlayingTrackRequest.build(additional_types=[SpotifyItemType.ALBUM])
