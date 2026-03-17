from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import GetPlaylistItemsRequest
from spotantic.models.playlists.requests import GetPlaylistItemsRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType


def test_get_playlist_items_request_model_validates_limit_and_offset(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
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


def test_get_playlist_items_request_model_rejects_bad_limit(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    with pytest.raises(ValidationError):
        GetPlaylistItemsRequest.build(playlist_id=example_id, limit=0, offset=0)

    with pytest.raises(ValidationError):
        GetPlaylistItemsRequest.build(playlist_id=example_id, limit=51, offset=0)


def test_get_playlist_items_request_model_rejects_invalid_additional_types(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    with pytest.raises(ValidationError):
        GetPlaylistItemsRequest.build(
            playlist_id=example_id,
            additional_types=[SpotifyItemType.SHOW],
        )
