from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import CreatePlaylistRequest
from spotantic.models.playlists.requests import CreatePlaylistRequestBody
from spotantic.models.playlists.requests import CreatePlaylistRequestParams
from spotantic.types import AuthScope


def test_create_playlist_request_model() -> None:
    user_id = "u1"
    name = "My Playlist"
    req = CreatePlaylistRequest.build(user_id=user_id, name=name, public=True)

    assert req.endpoint == f"users/{user_id}/playlists"
    assert req.method_type is HTTPMethod.POST
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in req.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in req.required_scopes
    assert req.headers.content_type == "application/json"

    body = req.body
    assert isinstance(body, CreatePlaylistRequestBody)
    assert body.name == name
    assert body.public is True

    params = req.params
    assert isinstance(params, CreatePlaylistRequestParams)
    assert params.user_id == user_id


def test_create_playlist_request_model_rejects_invalid_flag_combo() -> None:
    with pytest.raises(ValidationError):
        CreatePlaylistRequest.build(user_id="u1", name="My Playlist", public=False, collaborative=True)
