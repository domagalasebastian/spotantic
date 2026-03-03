from unittest import mock

import pytest

from spotantic.endpoints.albums import save_albums_for_current_user
from spotantic.models.albums.requests import SaveAlbumsForCurrentUserRequest


@pytest.mark.asyncio
async def test_save_albums_for_current_user_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(SaveAlbumsForCurrentUserRequest, "build", return_value=request_obj) as build_mock:
        result = await save_albums_for_current_user(client, album_ids=["a1", "a2"])

        build_mock.assert_called_once_with(album_ids=["a1", "a2"])
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
