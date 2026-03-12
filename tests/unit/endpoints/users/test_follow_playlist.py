from unittest import mock

import pytest

from spotantic.endpoints.users import follow_playlist
from spotantic.models.users.requests import FollowPlaylistRequest


@pytest.mark.asyncio
async def test_follow_playlist_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(FollowPlaylistRequest, "build", return_value=request_obj) as build_mock:
        result = await follow_playlist(client, playlist_id="playlist123", public=True)

        build_mock.assert_called_once_with(
            playlist_id="playlist123",
            public=True,
        )
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
