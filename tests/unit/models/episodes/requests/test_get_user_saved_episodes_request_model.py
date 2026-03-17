from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.episodes.requests import GetUserSavedEpisodesRequest
from spotantic.models.episodes.requests import GetUserSavedEpisodesRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyMarketID


def test_get_user_saved_episodes_request(example_instances_of_type):
    market = example_instances_of_type[SpotifyMarketID]
    req = GetUserSavedEpisodesRequest.build(limit=10, offset=2, market=market)

    assert req.endpoint == "me/episodes"
    assert AuthScope.USER_LIBRARY_READ in req.required_scopes
    assert AuthScope.USER_READ_PLAYBACK_POSITION in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetUserSavedEpisodesRequestParams)
    assert params.market == market
    assert params.limit == 10
    assert params.offset == 2
    assert req.body is None

    with pytest.raises(ValidationError):
        GetUserSavedEpisodesRequest.build(limit=0)
    with pytest.raises(ValidationError):
        GetUserSavedEpisodesRequest.build(limit=51)
