from http import HTTPMethod

from spotantic.models.tracks.requests import GetTrackRequest
from spotantic.models.tracks.requests import GetTrackRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID
from tests.unit._helpers import _example_instances_of_type


def test_get_track_request():
    track_id = _example_instances_of_type[SpotifyItemID]
    market = _example_instances_of_type[SpotifyMarketID]
    request = GetTrackRequest.build(track_id=track_id, market=market)

    assert request.endpoint == f"tracks/{track_id}"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetTrackRequestParams)
    assert params.track_id == track_id
    assert params.market == market
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == track_id
    assert params_dump["market"] == market
