from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.episodes.requests import GetSeveralEpisodesRequest
from spotantic.models.episodes.requests import GetSeveralEpisodesRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_get_several_episodes_request():
    example_id = _example_instances_of_type[SpotifyItemID]
    req = GetSeveralEpisodesRequest.build(episode_ids=[example_id, example_id], market="US")

    assert req.endpoint == "episodes"
    assert AuthScope.USER_READ_PLAYBACK_POSITION in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetSeveralEpisodesRequestParams)
    assert params.episode_ids == [example_id, example_id]
    assert params.market == "US"
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join([example_id, example_id])

    with pytest.raises(ValidationError):
        too_many = [example_id] * 51
        GetSeveralEpisodesRequest.build(episode_ids=too_many)
