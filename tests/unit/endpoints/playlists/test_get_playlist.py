from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.playlists import get_playlist
from spotantic.models.playlists.requests import GetPlaylistRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
async def test_get_playlist_builds_request_and_returns_model():
    client = mock.AsyncMock()
    fake_response = {"id": "p1"}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(id="p1")

    with mock.patch.object(GetPlaylistRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.spotify.PlaylistModel.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await get_playlist(
                client,
                playlist_id="p1",
                fields="name,tracks",
                additional_types=[SpotifyItemType.TRACK],
                market="US",
            )

            build_mock.assert_called_once_with(
                playlist_id="p1",
                fields="name,tracks",
                additional_types=[SpotifyItemType.TRACK],
                market="US",
            )
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
