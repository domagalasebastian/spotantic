from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.episodes.requests import RemoveUserSavedEpisodesRequest
from spotantic.models.episodes.requests import RemoveUserSavedEpisodesRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_remove_user_saved_episodes_request():
    example_id = _example_instances_of_type[SpotifyItemID]
    req = RemoveUserSavedEpisodesRequest.build(episode_ids=[example_id, example_id])

    assert req.endpoint == "me/episodes"
    assert AuthScope.USER_LIBRARY_MODIFY in req.required_scopes
    assert req.method_type is HTTPMethod.DELETE

    params = req.params
    assert isinstance(params, RemoveUserSavedEpisodesRequestParams)
    assert params.episode_ids == [example_id, example_id]
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join([example_id, example_id])

    with pytest.raises(ValidationError):
        too_many = [example_id] * 51
        RemoveUserSavedEpisodesRequest.build(episode_ids=too_many)
