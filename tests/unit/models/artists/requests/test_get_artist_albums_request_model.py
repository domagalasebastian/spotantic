from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.artists.requests import GetArtistAlbumsRequest
from spotantic.models.artists.requests import GetArtistAlbumsRequestParams
from spotantic.types import AlbumTypes
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


def test_get_artist_albums_request(example_instances_of_type):
    artist_id = example_instances_of_type[SpotifyItemID]
    market = example_instances_of_type[SpotifyMarketID]
    include = [AlbumTypes.ALBUM, AlbumTypes.SINGLE]
    request = GetArtistAlbumsRequest.build(
        artist_id=artist_id,
        limit=15,
        offset=2,
        market=market,
        include_groups=include,
    )

    assert request.endpoint == f"artists/{artist_id}/albums"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetArtistAlbumsRequestParams)
    assert params.artist_id == artist_id
    assert params.limit == 15
    assert params.offset == 2
    assert params.market == market
    assert params.include_groups == include
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == artist_id
    assert params_dump["limit"] == 15
    assert params_dump["offset"] == 2
    assert params_dump["include_groups"] == "album,single"

    with pytest.raises(ValidationError):
        request = GetArtistAlbumsRequest.build(
            artist_id=artist_id,
            limit=0,
            offset=2,
            market=market,
            include_groups=include,
        )

    with pytest.raises(ValidationError):
        request = GetArtistAlbumsRequest.build(
            artist_id=artist_id,
            limit=51,
            offset=2,
            market=market,
            include_groups=include,
        )
