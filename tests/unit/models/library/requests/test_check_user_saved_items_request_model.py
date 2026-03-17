from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.library.requests import CheckUserSavedItemsRequest
from spotantic.models.library.requests import CheckUserSavedItemsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyTrackURI


def test_check_user_saved_items_request_model(example_instances_of_type):
    example_uri = example_instances_of_type[SpotifyTrackURI]

    req = CheckUserSavedItemsRequest.build(uris=[example_uri, example_uri])

    assert req.endpoint == "me/library/contains"
    assert AuthScope.USER_LIBRARY_READ in req.required_scopes
    assert AuthScope.USER_FOLLOW_READ in req.required_scopes
    assert AuthScope.PLAYLIST_READ_PRIVATE in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, CheckUserSavedItemsRequestParams)
    assert params.uris == [example_uri, example_uri]
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["uris"] == ",".join([example_uri, example_uri])


def test_check_user_saved_items_request_model_rejects_too_many_uris(example_instances_of_type):
    example_uri = example_instances_of_type[SpotifyTrackURI]

    with pytest.raises(ValidationError):
        too_many = [example_uri] * 41
        CheckUserSavedItemsRequest.build(uris=too_many)
