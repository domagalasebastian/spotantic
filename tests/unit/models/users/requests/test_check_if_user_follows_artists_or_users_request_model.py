from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.users.requests import CheckIfUserFollowsArtistsOrUsersRequest
from spotantic.models.users.requests import CheckIfUserFollowsArtistsOrUsersRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemType


def test_check_if_user_follows_artists_or_users_request_artist():
    request = CheckIfUserFollowsArtistsOrUsersRequest.build(
        item_type=SpotifyItemType.ARTIST,
        item_ids=["a1", "a2"],
    )

    assert request.endpoint == "me/following/contains"
    assert request.method_type is HTTPMethod.GET
    assert AuthScope.USER_FOLLOW_READ in request.required_scopes

    params = request.params
    assert isinstance(params, CheckIfUserFollowsArtistsOrUsersRequestParams)
    assert params.item_type == SpotifyItemType.ARTIST
    assert params.item_ids == ["a1", "a2"]
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["type"] == "artist"
    assert params_dump["ids"] == "a1,a2"


def test_check_if_user_follows_artists_or_users_request_user():
    request = CheckIfUserFollowsArtistsOrUsersRequest.build(
        item_type=SpotifyItemType.USER,
        item_ids=["u1", "u2"],
    )

    assert request.endpoint == "me/following/contains"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, CheckIfUserFollowsArtistsOrUsersRequestParams)
    assert params.item_type == SpotifyItemType.USER
    assert params.item_ids == ["u1", "u2"]
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["type"] == "user"
    assert params_dump["ids"] == "u1,u2"


def test_check_if_user_follows_artists_or_users_request_too_many_ids():
    with pytest.raises(ValidationError):
        CheckIfUserFollowsArtistsOrUsersRequest.build(
            item_type=SpotifyItemType.ARTIST,
            item_ids=["a"] * 51,
        )


def test_check_if_user_follows_artists_or_users_request_invalid_type():
    with pytest.raises(ValidationError):
        CheckIfUserFollowsArtistsOrUsersRequest.build(
            item_type=SpotifyItemType.TRACK,
            item_ids=["a1"],
        )
