from pathlib import Path
from unittest import mock

import pytest

from spotantic.endpoints.playlists import add_custom_playlist_cover_image
from spotantic.models.playlists.requests import AddCustomPlaylistCoverImageRequest


@pytest.mark.asyncio
async def test_add_custom_playlist_cover_image_builds_request_and_returns_none_data(tmp_path: Path):
    client = mock.AsyncMock()
    fake_response = None
    client.request.return_value = fake_response

    request_obj = object()
    file_path = tmp_path / "img.jpg"
    file_path.write_bytes(b"JPEGDATA")

    with mock.patch.object(AddCustomPlaylistCoverImageRequest, "build", return_value=request_obj) as build_mock:
        result = await add_custom_playlist_cover_image(client, playlist_id="p1", file_path=file_path)

        build_mock.assert_called_once_with(playlist_id="p1", image_data=None, file_path=file_path)
        client.request.assert_awaited_once_with(request_obj)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is None
