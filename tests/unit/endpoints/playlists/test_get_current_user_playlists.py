from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.playlists import get_current_user_playlist
from spotantic.models.playlists.requests import GetCurrentUserPlaylistsRequest


@pytest.mark.asyncio
async def test_get_current_user_playlists_builds_request_and_returns_model():
    client = mock.AsyncMock()
    fake_response = {"items": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(items=[])

    with mock.patch.object(GetCurrentUserPlaylistsRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.spotify.PagedResultModel.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await get_current_user_playlist(client, limit=10, offset=5)

            build_mock.assert_called_once_with(limit=10, offset=5)
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
