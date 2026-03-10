from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import GetPlaylistItemsRequest
from spotantic.models.playlists.requests import GetPlaylistItemsRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType
from tests.unit._helpers import _example_instances_of_type


def test_get_playlist_items_request_model_validates_limit_and_offset() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]
    limit = 10
    offset = 5
    market = "US"
    req = GetPlaylistItemsRequest.build(
        playlist_id=example_id,
        limit=limit,
        offset=offset,
        additional_types=[SpotifyItemType.TRACK, SpotifyItemType.EPISODE],
        market=market,
    )

    assert req.endpoint == f"playlists/{example_id}/items"
    assert req.method_type is HTTPMethod.GET
    params = req.params
    assert isinstance(params, GetPlaylistItemsRequestParams)
    assert params.limit == limit
    assert params.offset == offset
    assert params.market == market

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["additional_types"] == "track,episode"


def test_get_playlist_items_request_model_rejects_bad_limit() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]
    with pytest.raises(ValidationError):
        GetPlaylistItemsRequest.build(playlist_id=example_id, limit=0, offset=0)

    with pytest.raises(ValidationError):
        GetPlaylistItemsRequest.build(playlist_id=example_id, limit=51, offset=0)


def test_get_playlist_items_request_model_rejects_invalid_additional_types() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]
    with pytest.raises(ValidationError):
        GetPlaylistItemsRequest.build(
            playlist_id=example_id,
            additional_types=[SpotifyItemType.SHOW],
        )
