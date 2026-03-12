from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.tracks.requests import GetUserSavedTracksRequest
from spotantic.models.tracks.requests import GetUserSavedTracksRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyMarketID
from tests.unit._helpers import _example_instances_of_type


def test_get_user_saved_tracks_request():
    market = _example_instances_of_type[SpotifyMarketID]
    limit = 50
    offset = 10
    request = GetUserSavedTracksRequest.build(limit=limit, offset=offset, market=market)

    assert request.endpoint == "me/tracks"
    assert AuthScope.USER_LIBRARY_READ in request.required_scopes
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetUserSavedTracksRequestParams)
    assert params.limit == limit
    assert params.offset == offset
    assert params.market == market
    assert request.body is None


def test_get_user_saved_tracks_request_model_rejects_invalid_limit_and_offset() -> None:
    with pytest.raises(ValidationError):
        GetUserSavedTracksRequest.build(limit=0, offset=0)

    with pytest.raises(ValidationError):
        GetUserSavedTracksRequest.build(limit=51, offset=0)
