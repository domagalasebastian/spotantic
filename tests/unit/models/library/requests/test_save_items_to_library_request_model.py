from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.library.requests import SaveItemsToLibraryRequest
from spotantic.models.library.requests import SaveItemsToLibraryRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyTrackURI
from tests.unit._helpers import _example_instances_of_type


def test_save_items_to_library_request_model():
    example_uri = _example_instances_of_type[SpotifyTrackURI]

    req = SaveItemsToLibraryRequest.build(uris=[example_uri, example_uri])

    assert req.endpoint == "me/library"
    assert AuthScope.USER_LIBRARY_MODIFY in req.required_scopes
    assert AuthScope.USER_FOLLOW_MODIFY in req.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, SaveItemsToLibraryRequestParams)
    assert params.uris == [example_uri, example_uri]
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["uris"] == ",".join([example_uri, example_uri])


def test_save_items_to_library_request_model_rejects_too_many_uris():
    example_uri = _example_instances_of_type[SpotifyTrackURI]

    with pytest.raises(ValidationError):
        too_many = [example_uri] * 41
        SaveItemsToLibraryRequest.build(uris=too_many)
