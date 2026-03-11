from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.search.requests import SearchForItemIncludeExternal
from spotantic.models.search.requests import SearchForItemRequest
from spotantic.models.search.requests import SearchForItemRequestParams
from spotantic.types import SpotifyItemType


def test_search_for_item_request_model_serializes_query_and_params() -> None:
    query = "test"
    item_type = [SpotifyItemType.TRACK, SpotifyItemType.ALBUM]
    market = "US"
    limit = 5
    offset = 10
    include_external = SearchForItemIncludeExternal.AUDIO
    req = SearchForItemRequest.build(
        query=query,
        item_type=item_type,
        market=market,
        limit=limit,
        offset=offset,
        include_external=include_external,
    )

    assert req.endpoint == "search"
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, SearchForItemRequestParams)
    assert params.query == query
    assert params.item_type == item_type
    assert params.market == market
    assert params.limit == limit
    assert params.offset == offset
    assert params.include_external == include_external

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["type"] == "track,album"
    assert params_dump["include_external"] == "audio"


def test_search_for_item_request_model_rejects_unsupported_item_type() -> None:
    with pytest.raises(ValidationError):
        SearchForItemRequest.build(query="test", item_type=[SpotifyItemType.USER])


def test_search_for_item_request_model_rejects_invalid_limit_and_offset() -> None:
    with pytest.raises(ValidationError):
        SearchForItemRequest.build(query="test", item_type=[SpotifyItemType.TRACK], limit=0)

    with pytest.raises(ValidationError):
        SearchForItemRequest.build(query="test", item_type=[SpotifyItemType.TRACK], limit=11)

    with pytest.raises(ValidationError):
        SearchForItemRequest.build(query="test", item_type=[SpotifyItemType.TRACK], offset=-1)

    with pytest.raises(ValidationError):
        SearchForItemRequest.build(query="test", item_type=[SpotifyItemType.TRACK], offset=1001)
