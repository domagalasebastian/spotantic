from http import HTTPMethod

import pytest

from spotantic.models.shows.requests import RemoveUserSavedShowsRequest
from spotantic.models.shows.requests import RemoveUserSavedShowsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_remove_user_saved_shows_request_model_serializes_ids_and_market(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    req = RemoveUserSavedShowsRequest.build(show_ids=[example_id, example_id], market="US")

    assert req.endpoint == "me/shows"
    assert AuthScope.USER_LIBRARY_MODIFY in req.required_scopes
    assert req.method_type is HTTPMethod.DELETE

    params = req.params
    assert isinstance(params, RemoveUserSavedShowsRequestParams)
    assert params.show_ids == [example_id, example_id]
    assert params.market == "US"

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join([example_id, example_id])


def test_remove_user_saved_shows_request_model_rejects_too_many_ids(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]

    with pytest.raises(Exception):
        too_many = [example_id] * 51
        RemoveUserSavedShowsRequest.build(show_ids=too_many)
