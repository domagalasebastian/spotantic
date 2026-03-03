from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.albums.requests import RemoveUserSavedAlbumsRequest
from spotantic.models.albums.requests import RemoveUserSavedAlbumsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from tests.unit._helpers import _example_instances_of_type


def test_remove_user_saved_albums_request():
    example_album_id = _example_instances_of_type[SpotifyItemID]
    album_ids = [example_album_id, example_album_id]
    req = RemoveUserSavedAlbumsRequest.build(album_ids=album_ids)

    assert req.endpoint == "me/albums"
    assert AuthScope.USER_LIBRARY_MODIFY in req.required_scopes
    assert req.method_type is HTTPMethod.DELETE

    params = req.params
    assert isinstance(params, RemoveUserSavedAlbumsRequestParams)
    assert params.album_ids == album_ids
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join(album_ids)

    with pytest.raises(ValidationError):
        too_many_ids = [example_album_id] * 21
        RemoveUserSavedAlbumsRequest.build(album_ids=too_many_ids)
