from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.albums.requests import GetAlbumTracksRequest
from spotantic.models.albums.requests import GetAlbumTracksRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


def test_get_album_tracks_request(example_instances_of_type):
    album_id = example_instances_of_type[SpotifyItemID]
    market = example_instances_of_type[SpotifyMarketID]
    limit = 20
    offset = 0
    request = GetAlbumTracksRequest.build(
        album_id=album_id,
        market=market,
        limit=limit,
        offset=offset,
    )

    assert request.endpoint == f"albums/{album_id}/tracks"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetAlbumTracksRequestParams)
    assert params.album_id == album_id
    assert params.market == market
    assert params.limit == 20
    assert params.offset == 0
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == album_id

    with pytest.raises(ValidationError):
        GetAlbumTracksRequest.build(
            album_id=album_id,
            limit=0,
        )

    with pytest.raises(ValidationError):
        GetAlbumTracksRequest.build(
            album_id=album_id,
            limit=51,
        )
