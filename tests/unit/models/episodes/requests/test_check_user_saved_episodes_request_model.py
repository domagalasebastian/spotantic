from http import HTTPMethod

import pytest

from spotantic.models.episodes.requests import CheckUserSavedEpisodesRequest
from spotantic.models.episodes.requests import CheckUserSavedEpisodesRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_check_user_saved_episodes_request():
    example_id = _example_instances_of_type[SpotifyItemID]
    req = CheckUserSavedEpisodesRequest.build(episode_ids=[example_id, example_id])

    assert req.endpoint == "me/episodes/contains"
    assert AuthScope.USER_LIBRARY_READ in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, CheckUserSavedEpisodesRequestParams)
    assert params.episode_ids == [example_id, example_id]
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join([example_id, example_id])

    with pytest.raises(Exception):
        too_many = [example_id] * 51
        CheckUserSavedEpisodesRequest.build(episode_ids=too_many)
