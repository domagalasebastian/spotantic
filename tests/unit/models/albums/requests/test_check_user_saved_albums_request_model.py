from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.albums.requests import CheckUserSavedAlbumsRequest
from spotantic.models.albums.requests import CheckUserSavedAlbumsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_check_user_saved_albums_request(example_instances_of_type):
    example_album_id = example_instances_of_type[SpotifyItemID]
    album_ids = [example_album_id, example_album_id]
    req = CheckUserSavedAlbumsRequest.build(album_ids=album_ids)
    assert req.endpoint == "me/albums/contains"
    assert AuthScope.USER_LIBRARY_READ in req.required_scopes
    assert req.method_type is HTTPMethod.GET

    params = req.params
    assert isinstance(params, CheckUserSavedAlbumsRequestParams)
    assert params.album_ids == album_ids
    assert req.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["ids"] == ",".join(album_ids)

    with pytest.raises(ValidationError):
        too_many_ids = [example_album_id] * 21
        CheckUserSavedAlbumsRequest.build(album_ids=too_many_ids)
