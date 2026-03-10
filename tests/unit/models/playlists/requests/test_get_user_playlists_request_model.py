from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import GetUserPlaylistsRequest
from spotantic.models.playlists.requests import GetUserPlaylistsRequestParams
from spotantic.types import AuthScope


def test_get_user_playlists_request_model_validates_range() -> None:
    user_id = "u1"
    limit = 10
    offset = 5
    req = GetUserPlaylistsRequest.build(user_id=user_id, limit=limit, offset=offset)

    assert req.endpoint == f"users/{user_id}/playlists"
    assert req.method_type is HTTPMethod.GET
    assert AuthScope.PLAYLIST_READ_PRIVATE in req.required_scopes

    params = req.params
    assert isinstance(params, GetUserPlaylistsRequestParams)
    assert params.user_id == user_id
    assert params.limit == limit
    assert params.offset == offset


def test_get_user_playlists_request_model_rejects_invalid_limit_and_offset() -> None:
    with pytest.raises(ValidationError):
        GetUserPlaylistsRequest.build(user_id="u1", limit=0, offset=0)

    with pytest.raises(ValidationError):
        GetUserPlaylistsRequest.build(user_id="u1", limit=51, offset=0)

    with pytest.raises(ValidationError):
        GetUserPlaylistsRequest.build(user_id="u1", limit=1, offset=-1)

    with pytest.raises(ValidationError):
        GetUserPlaylistsRequest.build(user_id="u1", limit=1, offset=100_001)
