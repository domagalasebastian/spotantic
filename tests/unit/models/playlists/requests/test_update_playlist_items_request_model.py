from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import UpdatePlaylistItemsRequest
from spotantic.models.playlists.requests import UpdatePlaylistItemsRequestBody
from spotantic.models.playlists.requests import UpdatePlaylistItemsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyTrackURI


def test_update_playlist_items_request_model_serializes_uris_and_range_params(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    example_uri = example_instances_of_type[SpotifyTrackURI]
    range_start = 0
    insert_before = 1
    range_length = 2
    snapshot_id = "s1"
    req = UpdatePlaylistItemsRequest.build(
        playlist_id=example_id,
        uris=[example_uri],
        range_start=range_start,
        insert_before=insert_before,
        range_length=range_length,
        snapshot_id=snapshot_id,
    )

    assert req.endpoint == f"playlists/{example_id}/items"
    assert req.method_type is HTTPMethod.PUT
    assert req.headers.content_type == "application/json"
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in req.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in req.required_scopes

    body = req.body
    assert isinstance(body, UpdatePlaylistItemsRequestBody)
    assert body.range_start == range_start
    assert body.insert_before == insert_before
    assert body.range_length == range_length
    assert body.snapshot_id == snapshot_id
    assert body.uris == [example_uri]

    params = req.params
    assert isinstance(params, UpdatePlaylistItemsRequestParams)
    params_dump = params.model_dump(by_alias=True)
    assert params_dump["id"] == example_id


def test_update_playlist_items_request_model_rejects_too_many_uris(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    example_uri = example_instances_of_type[SpotifyTrackURI]
    uris = [example_uri] * 101
    with pytest.raises(ValidationError):
        UpdatePlaylistItemsRequest.build(
            playlist_id=example_id,
            uris=uris,
            range_start=0,
            insert_before=1,
        )
