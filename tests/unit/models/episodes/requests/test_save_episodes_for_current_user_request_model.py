from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.episodes.requests import SaveEpisodesForCurrentUserRequest
from spotantic.models.episodes.requests import SaveEpisodesForCurrentUserRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_save_episodes_for_current_user_request(example_instances_of_type):
    example_id = example_instances_of_type[SpotifyItemID]
    req = SaveEpisodesForCurrentUserRequest.build(episode_ids=[example_id, example_id])

    assert req.endpoint == "me/episodes"
    assert AuthScope.USER_LIBRARY_MODIFY in req.required_scopes
    assert req.method_type is HTTPMethod.PUT

    params = req.params
    assert isinstance(params, SaveEpisodesForCurrentUserRequestParams)
    assert params.episode_ids == [example_id, example_id]
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join([example_id, example_id])

    with pytest.raises(ValidationError):
        too_many = [example_id] * 51
        SaveEpisodesForCurrentUserRequest.build(episode_ids=too_many)
