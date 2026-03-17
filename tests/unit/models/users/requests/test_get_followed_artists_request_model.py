from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.users.requests import GetFollowedArtistsRequest
from spotantic.models.users.requests import GetFollowedArtistsRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType


def test_get_followed_artists_request():
    request = GetFollowedArtistsRequest.build()

    assert request.endpoint == "me/following"
    assert request.method_type is HTTPMethod.GET
    assert AuthScope.USER_FOLLOW_READ in request.required_scopes

    params = request.params
    assert isinstance(params, GetFollowedArtistsRequestParams)
    assert params.item_type == SpotifyItemType.ARTIST
    assert params.after is None
    assert params.limit is None
    assert request.body is None


def test_get_followed_artists_request_with_after_and_limit(example_instances_of_type):
    after_id = example_instances_of_type[SpotifyItemID]
    request = GetFollowedArtistsRequest.build(
        item_type=SpotifyItemType.ARTIST,
        after=after_id,
        limit=50,
    )

    assert request.endpoint == "me/following"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetFollowedArtistsRequestParams)
    assert params.item_type == SpotifyItemType.ARTIST
    assert params.after == after_id
    assert params.limit == 50
    assert request.body is None

    params_dump = params.model_dump(by_alias=True)
    assert params_dump["type"] == SpotifyItemType.ARTIST.value
    assert params_dump["after"] == after_id
    assert params_dump["limit"] == 50


def test_get_followed_artists_request_invalid_type():
    with pytest.raises(ValidationError):
        GetFollowedArtistsRequest.build(item_type=SpotifyItemType.TRACK)


def test_get_followed_artists_request_limit_too_high():
    with pytest.raises(ValidationError):
        GetFollowedArtistsRequest.build(limit=51)


def test_get_followed_artists_request_limit_too_low():
    with pytest.raises(ValidationError):
        GetFollowedArtistsRequest.build(limit=0)
