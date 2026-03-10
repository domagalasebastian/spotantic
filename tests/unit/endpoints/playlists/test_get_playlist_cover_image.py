from unittest import mock

import pytest

from spotantic.endpoints.playlists import get_playlist_cover_image
from spotantic.models.playlists.requests import GetPlaylistCoverImageRequest


@pytest.mark.asyncio
async def test_get_playlist_cover_image_builds_request_and_validates_list_response():
    client = mock.AsyncMock()
    fake_response = [{"url": "https://..."}]
    client.request_json.return_value = fake_response

    request_obj = object()

    with mock.patch.object(GetPlaylistCoverImageRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.endpoints.playlists._get_playlist_cover_image.validate_is_instance_of",
            return_value=fake_response,
        ) as validate_mock:
            result = await get_playlist_cover_image(client, playlist_id="p1")

            build_mock.assert_called_once_with(playlist_id="p1")
            client.request_json.assert_awaited_once_with(request_obj)
            assert validate_mock.call_count == 1
            assert validate_mock.call_args[0][0] == fake_response

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data == fake_response
