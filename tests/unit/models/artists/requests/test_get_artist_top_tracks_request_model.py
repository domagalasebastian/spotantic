from http import HTTPMethod

from spotantic.models.artists.requests import GetArtistTopTracksRequest
from spotantic.models.artists.requests import GetArtistTopTracksRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


def test_get_artist_top_tracks_request(example_instances_of_type):
    artist_id = example_instances_of_type[SpotifyItemID]
    market = example_instances_of_type[SpotifyMarketID]
    request = GetArtistTopTracksRequest.build(artist_id=artist_id, market=market)

    assert request.endpoint == f"artists/{artist_id}/top-tracks"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetArtistTopTracksRequestParams)
    assert params.artist_id == artist_id
    assert params.market == market
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == artist_id
