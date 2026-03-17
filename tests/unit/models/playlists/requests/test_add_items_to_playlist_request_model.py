from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import AddItemsToPlaylistRequest
from spotantic.models.playlists.requests import AddItemsToPlaylistRequestBody
from spotantic.models.playlists.requests import AddItemsToPlaylistRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyTrackURI


def test_add_items_to_playlist_request_model(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    example_uri = example_instances_of_type[SpotifyTrackURI]
    req = AddItemsToPlaylistRequest.build(playlist_id=example_id, uris=[example_uri], position=2)

    assert req.endpoint == f"playlists/{example_id}/items"
    assert req.method_type is HTTPMethod.POST
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in req.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in req.required_scopes
    assert req.headers.content_type == "application/json"

    body = req.body
    assert isinstance(body, AddItemsToPlaylistRequestBody)
    assert body.uris == [example_uri]
    assert body.position == 2

    assert isinstance(req.params, AddItemsToPlaylistRequestParams)
    params_dump = req.params.model_dump(by_alias=True)
    assert params_dump["id"] == example_id


def test_add_items_to_playlist_request_model_rejects_too_many_uris(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    example_uri = example_instances_of_type[SpotifyTrackURI]
    uris = [example_uri * 101]
    with pytest.raises(ValidationError):
        AddItemsToPlaylistRequest.build(playlist_id=example_id, uris=uris)
