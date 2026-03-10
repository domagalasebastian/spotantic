from http import HTTPMethod

import pytest

from spotantic.models.playlists.requests import GetPlaylistRequest
from spotantic.models.playlists.requests import GetPlaylistRequestParams
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType
from tests.unit._helpers import _example_instances_of_type


def test_get_playlist_request_model_serializes_additional_types() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]
    fields = "name"
    market = "US"
    req = GetPlaylistRequest.build(
        playlist_id=example_id,
        fields=fields,
        additional_types=[SpotifyItemType.TRACK, SpotifyItemType.EPISODE],
        market=market,
    )

    assert req.endpoint == f"playlists/{example_id}"
    assert req.method_type is HTTPMethod.GET
    params = req.params
    assert isinstance(params, GetPlaylistRequestParams)
    assert params.playlist_id == example_id
    assert params.fields == fields
    assert params.market == market

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["additional_types"] == "track,episode"
    assert params_dump["id"] == example_id


def test_get_playlist_request_model_rejects_unsupported_item_type() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]
    with pytest.raises(ValueError):
        GetPlaylistRequest.build(
            playlist_id=example_id,
            additional_types=[SpotifyItemType.ALBUM],
        )
