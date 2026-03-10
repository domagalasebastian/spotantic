from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.player.requests import GetRecentlyPlayedTracksRequest
from spotantic.models.player.requests import GetRecentlyPlayedTracksRequestParams
from spotantic.types import AuthScope


def test_get_recently_played_tracks_request_model_defaults_and_validation() -> None:
    req = GetRecentlyPlayedTracksRequest.build(limit=10)

    assert req.endpoint == "me/player/recently-played"
    assert AuthScope.USER_READ_RECENTLY_PLAYED in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetRecentlyPlayedTracksRequestParams)
    assert params.limit == 10
    assert params.after is None
    assert params.before is None


def test_get_recently_played_tracks_request_model_rejects_both_after_and_before() -> None:
    with pytest.raises(ValueError):
        GetRecentlyPlayedTracksRequest.build(limit=10, after=123, before=456)


def test_get_recently_played_tracks_request_model_rejects_invalid_limit() -> None:
    with pytest.raises(ValidationError):
        GetRecentlyPlayedTracksRequest.build(limit=0)
