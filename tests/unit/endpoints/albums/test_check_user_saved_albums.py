from unittest import mock

import pytest

from spotantic.endpoints.albums import check_user_saved_albums
from spotantic.models.albums.requests import CheckUserSavedAlbumsRequest


@pytest.mark.asyncio
async def test_check_user_saved_albums_builds_request_and_returns_mapping():
    client = mock.AsyncMock()
    fake_response = [True, False]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(CheckUserSavedAlbumsRequest, "build", return_value=request_obj) as build_mock:
        result = await check_user_saved_albums(client, album_ids=["a1", "a2"])

        build_mock.assert_called_once_with(album_ids=["a1", "a2"])
        client.request_json.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data == {"a1": True, "a2": False}
