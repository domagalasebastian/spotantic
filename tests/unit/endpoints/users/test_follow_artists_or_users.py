from unittest import mock

import pytest

from spotantic.endpoints.users import follow_artists_or_users
from spotantic.models.users.requests import FollowArtistsOrUsersRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
async def test_follow_artists_or_users_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(FollowArtistsOrUsersRequest, "build", return_value=request_obj) as build_mock:
        result = await follow_artists_or_users(
            client,
            item_type=SpotifyItemType.ARTIST,
            item_ids=["a1", "a2"],
        )

        build_mock.assert_called_once_with(
            item_type=SpotifyItemType.ARTIST,
            item_ids=["a1", "a2"],
        )
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
