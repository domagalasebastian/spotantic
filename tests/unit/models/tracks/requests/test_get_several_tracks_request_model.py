from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.tracks.requests import GetSeveralTracksRequest
from spotantic.models.tracks.requests import GetSeveralTracksRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID
from tests.unit._helpers import _example_instances_of_type


def test_get_several_tracks_request():
    example_track_id = _example_instances_of_type[SpotifyItemID]
    example_market = _example_instances_of_type[SpotifyMarketID]
    track_ids = [example_track_id, example_track_id]
    request = GetSeveralTracksRequest.build(track_ids=track_ids, market=example_market)

    assert request.endpoint == "tracks"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetSeveralTracksRequestParams)
    assert params.track_ids == track_ids
    assert params.market == example_market
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join(track_ids)
    assert params_dump["market"] == example_market


def test_get_several_tracks_request_too_many_ids():
    example_track_id = _example_instances_of_type[SpotifyItemID]
    too_many_ids = [example_track_id] * 51

    with pytest.raises(ValidationError):
        GetSeveralTracksRequest.build(track_ids=too_many_ids)
