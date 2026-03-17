from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.shows.requests import GetShowEpisodesRequest
from spotantic.models.shows.requests import GetShowEpisodesRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_get_show_episodes_request_model_serializes_params(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]

    req = GetShowEpisodesRequest.build(show_id=example_id, limit=5, offset=2, market="US")

    assert req.endpoint == f"shows/{example_id}/episodes"
    assert AuthScope.USER_READ_PLAYBACK_POSITION in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetShowEpisodesRequestParams)
    assert params.show_id == example_id
    assert params.limit == 5
    assert params.offset == 2
    assert params.market == "US"


def test_get_show_episodes_request_model_rejects_invalid_limit(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]

    with pytest.raises(ValidationError):
        GetShowEpisodesRequest.build(show_id=example_id, limit=0, offset=0)

    with pytest.raises(ValidationError):
        GetShowEpisodesRequest.build(show_id=example_id, limit=51, offset=0)
