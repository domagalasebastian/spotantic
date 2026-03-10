from unittest import mock

import pytest

from spotantic.endpoints.playlists import change_playlist_details
from spotantic.models.playlists.requests import ChangePlaylistDetailsRequest


@pytest.mark.asyncio
async def test_change_playlist_details_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(ChangePlaylistDetailsRequest, "build", return_value=request_obj) as build_mock:
        result = await change_playlist_details(
            client, playlist_id="p1", name="New", public=True, collaborative=False, description="desc"
        )

        build_mock.assert_called_once_with(
            playlist_id="p1",
            name="New",
            public=True,
            collaborative=False,
            description="desc",
        )
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
