from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import RemovePlaylistItemsRequest
from spotantic.models.playlists.requests import RemovePlaylistItemsRequestBody
from spotantic.models.playlists.requests import RemovePlaylistItemsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyTrackURI
from tests.unit._helpers import _example_instances_of_type


def test_remove_playlist_items_request_model_serializes_tracks() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]
    example_uri = _example_instances_of_type[SpotifyTrackURI]
    snapshot_id = "s1"
    req = RemovePlaylistItemsRequest.build(playlist_id=example_id, uris=[example_uri], snapshot_id=snapshot_id)

    assert req.endpoint == f"playlists/{example_id}/items"
    assert req.method_type is HTTPMethod.DELETE
    assert req.headers.content_type == "application/json"
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in req.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in req.required_scopes

    body = req.body
    assert isinstance(body, RemovePlaylistItemsRequestBody)
    assert body.snapshot_id == snapshot_id
    assert body.tracks == [example_uri]

    body_dump = body.model_dump(by_alias=True)
    assert body_dump["tracks"] == [{"uri": example_uri}]

    params = req.params
    assert isinstance(params, RemovePlaylistItemsRequestParams)
    assert params.playlist_id == example_id


def test_remove_playlist_items_request_model_rejects_too_many_uris() -> None:
    example_id = _example_instances_of_type[SpotifyItemID]
    example_uri = _example_instances_of_type[SpotifyTrackURI]
    uris = [example_uri] * 101
    with pytest.raises(ValidationError):
        RemovePlaylistItemsRequest.build(playlist_id=example_id, uris=uris)
