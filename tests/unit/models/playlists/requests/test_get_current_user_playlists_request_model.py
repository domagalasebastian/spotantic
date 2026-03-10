from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import GetCurrentUserPlaylistsRequest
from spotantic.types import AuthScope


def test_get_current_user_playlists_request_model_validates_range() -> None:
    req = GetCurrentUserPlaylistsRequest.build(limit=10, offset=5)

    assert req.endpoint == "me/playlists"
    assert req.method_type is HTTPMethod.GET
    assert AuthScope.PLAYLIST_READ_PRIVATE in req.required_scopes


def test_get_current_user_playlists_request_model_rejects_invalid_limit_and_offset() -> None:
    with pytest.raises(ValidationError):
        GetCurrentUserPlaylistsRequest.build(limit=0, offset=0)

    with pytest.raises(ValidationError):
        GetCurrentUserPlaylistsRequest.build(limit=1, offset=-1)

    with pytest.raises(ValidationError):
        GetCurrentUserPlaylistsRequest.build(limit=1, offset=100_001)
