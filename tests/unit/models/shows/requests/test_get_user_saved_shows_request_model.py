from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.shows.requests import GetUserSavedShowsRequest
from spotantic.models.shows.requests import GetUserSavedShowsRequestParams
from spotantic.types import AuthScope


def test_get_user_saved_shows_request_model_serializes_params() -> None:
    req = GetUserSavedShowsRequest.build(limit=5, offset=2)

    assert req.endpoint == "me/shows"
    assert AuthScope.USER_LIBRARY_READ in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetUserSavedShowsRequestParams)
    assert params.limit == 5
    assert params.offset == 2


def test_get_user_saved_shows_request_model_rejects_invalid_limit_and_offset() -> None:
    with pytest.raises(ValidationError):
        GetUserSavedShowsRequest.build(limit=0, offset=0)

    with pytest.raises(ValidationError):
        GetUserSavedShowsRequest.build(limit=51, offset=0)
