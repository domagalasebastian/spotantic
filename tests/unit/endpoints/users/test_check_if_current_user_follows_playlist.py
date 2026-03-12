from unittest import mock

import pytest

from spotantic.endpoints.users import check_if_current_user_follows_playlist
from spotantic.models.users.requests import CheckIfCurrentUserFollowsPlaylistRequest


@pytest.mark.asyncio
async def test_check_if_current_user_follows_playlist_builds_request_and_returns_bool():
    client = mock.AsyncMock()
    fake_response = [True]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(CheckIfCurrentUserFollowsPlaylistRequest, "build", return_value=request_obj) as build_mock:
        result = await check_if_current_user_follows_playlist(
            client,
            playlist_id="playlist123",
        )

        build_mock.assert_called_once_with(
            playlist_id="playlist123",
        )
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is True
