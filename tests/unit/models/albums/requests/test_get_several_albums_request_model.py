from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.albums.requests import GetSeveralAlbumsRequest
from spotantic.models.albums.requests import GetSeveralAlbumsRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


def test_get_several_albums_request(example_instances_of_type):
    example_album_id = example_instances_of_type[SpotifyItemID]
    album_ids = [example_album_id, example_album_id]
    market = example_instances_of_type[SpotifyMarketID]
    request = GetSeveralAlbumsRequest.build(album_ids=album_ids, market=market)

    assert request.endpoint == "albums"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetSeveralAlbumsRequestParams)
    assert params.album_ids == album_ids
    assert params.market == market
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join(album_ids)

    with pytest.raises(ValidationError):
        too_many_ids = [example_album_id] * 21
        GetSeveralAlbumsRequest.build(album_ids=too_many_ids)
