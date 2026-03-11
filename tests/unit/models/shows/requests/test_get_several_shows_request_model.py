from http import HTTPMethod

import pytest

from spotantic.models.shows.requests import GetSeveralShowsRequest
from spotantic.models.shows.requests import GetSeveralShowsRequestParams
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_get_several_shows_request_model_serializes_ids_and_market() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]

    req = GetSeveralShowsRequest.build(show_ids=[example_id, example_id], market="US")

    assert req.endpoint == "shows"
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, GetSeveralShowsRequestParams)
    assert params.show_ids == [example_id, example_id]
    assert params.market == "US"

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join([example_id, example_id])


def test_get_several_shows_request_model_rejects_too_many_ids() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]

    with pytest.raises(Exception):
        too_many = [example_id] * 51
        GetSeveralShowsRequest.build(show_ids=too_many)
