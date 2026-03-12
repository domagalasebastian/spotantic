from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.users.requests import FollowArtistsOrUsersRequest
from spotantic.models.users.requests import FollowArtistsOrUsersRequestBody
from spotantic.models.users.requests import FollowArtistsOrUsersRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemType


def test_follow_artists_or_users_request_artist():
    request = FollowArtistsOrUsersRequest.build(
        item_type=SpotifyItemType.ARTIST,
        item_ids=["a1", "a2"],
    )

    assert request.endpoint == "me/following"
    assert request.method_type is HTTPMethod.PUT
    assert AuthScope.USER_FOLLOW_MODIFY in request.required_scopes

    params = request.params
    assert isinstance(params, FollowArtistsOrUsersRequestParams)
    assert params.item_type == SpotifyItemType.ARTIST

    body = request.body
    assert isinstance(body, FollowArtistsOrUsersRequestBody)
    assert body.item_ids == ["a1", "a2"]


def test_follow_artists_or_users_request_user():
    request = FollowArtistsOrUsersRequest.build(
        item_type=SpotifyItemType.USER,
        item_ids=["u1", "u2"],
    )

    assert request.endpoint == "me/following"
    assert request.method_type is HTTPMethod.PUT

    params = request.params
    assert isinstance(params, FollowArtistsOrUsersRequestParams)
    assert params.item_type == SpotifyItemType.USER

    body = request.body
    assert isinstance(body, FollowArtistsOrUsersRequestBody)
    assert body.item_ids == ["u1", "u2"]


def test_follow_artists_or_users_request_too_many_ids():
    with pytest.raises(ValidationError):
        FollowArtistsOrUsersRequest.build(
            item_type=SpotifyItemType.ARTIST,
            item_ids=["a"] * 51,
        )


def test_follow_artists_or_users_request_invalid_type():
    with pytest.raises(ValidationError):
        FollowArtistsOrUsersRequest.build(
            item_type=SpotifyItemType.TRACK,
            item_ids=["a1"],
        )
