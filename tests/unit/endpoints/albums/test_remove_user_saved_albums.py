from unittest import mock

import pytest

from spotantic.endpoints.albums import remove_user_saved_albums
from spotantic.models.albums.requests import RemoveUserSavedAlbumsRequest


@pytest.mark.asyncio
async def test_remove_user_saved_albums_builds_request_and_returns_none_data():
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()

    with mock.patch.object(RemoveUserSavedAlbumsRequest, "build", return_value=request_obj) as build_mock:
        result = await remove_user_saved_albums(client, album_ids=["a1", "a2"])

        build_mock.assert_called_once_with(album_ids=["a1", "a2"])
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
