from http import HTTPMethod

from spotantic.models.albums.requests import GetAlbumRequest
from spotantic.models.albums.requests import GetAlbumRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID
from tests.unit._helpers import _example_instances_of_type


def test_get_album_request():
    album_id = _example_instances_of_type[SpotifyItemID]
    market = _example_instances_of_type[SpotifyMarketID]
    request = GetAlbumRequest.build(album_id=album_id, market=market)

    assert request.endpoint == f"albums/{album_id}"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetAlbumRequestParams)
    assert params.album_id == album_id
    assert params.market == market
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == album_id
