from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.playlists import create_playlist
from spotantic.models.playlists.requests import CreatePlaylistRequest


@pytest.mark.asyncio
async def test_create_playlist_builds_request_and_returns_model():
    client = mock.AsyncMock()
    fake_response = {"id": "p1"}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(id="p1")

    with mock.patch.object(CreatePlaylistRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.spotify.PlaylistModel.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await create_playlist(client, user_id="u1", name="My Playlist", public=True)

            build_mock.assert_called_once_with(
                user_id="u1",
                name="My Playlist",
                description=None,
                public=True,
                collaborative=None,
            )
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
