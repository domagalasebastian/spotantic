from unittest import mock

import pytest

from spotantic.endpoints.users import unfollow_playlist
from spotantic.models.users.requests import UnfollowPlaylistRequest


@pytest.mark.asyncio
async def test_unfollow_playlist_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(UnfollowPlaylistRequest, "build", return_value=request_obj) as build_mock:
        result = await unfollow_playlist(client, playlist_id="playlist123")

        build_mock.assert_called_once_with(
            playlist_id="playlist123",
        )
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
