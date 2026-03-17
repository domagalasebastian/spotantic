from http import HTTPMethod

import pytest

from spotantic.models.shows.requests import SaveShowsForCurrentUserRequest
from spotantic.models.shows.requests import SaveShowsForCurrentUserRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_save_shows_for_current_user_request_model_serializes_ids(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    req = SaveShowsForCurrentUserRequest.build(show_ids=[example_id, example_id])

    assert req.endpoint == "me/shows"
    assert AuthScope.USER_LIBRARY_MODIFY in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, SaveShowsForCurrentUserRequestParams)
    assert params.show_ids == [example_id, example_id]

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join([example_id, example_id])


def test_save_shows_for_current_user_request_model_rejects_too_many_ids(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]

    with pytest.raises(Exception):
        too_many = [example_id] * 51
        SaveShowsForCurrentUserRequest.build(show_ids=too_many)
