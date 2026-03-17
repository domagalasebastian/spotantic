from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.albums.requests import GetUserSavedAlbumsRequest
from spotantic.models.albums.requests import GetUserSavedAlbumsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyMarketID


def test_get_user_saved_albums_request(example_instances_of_type):
    market = example_instances_of_type[SpotifyMarketID]
    limit = 20
    offset = 0
    req = GetUserSavedAlbumsRequest.build(
        limit=limit,
        offset=offset,
        market=market,
    )

    assert req.endpoint == "me/albums"
    assert AuthScope.USER_LIBRARY_READ in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetUserSavedAlbumsRequestParams)
    assert params.market == market
    assert params.limit == 20
    assert params.offset == 0
    assert req.body is None

    with pytest.raises(ValidationError):
        GetUserSavedAlbumsRequest.build(
            limit=0,
        )

    with pytest.raises(ValidationError):
        GetUserSavedAlbumsRequest.build(
            limit=51,
        )
