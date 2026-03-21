from pathlib import Path

import pytest

from spotantic.endpoints.playlists import add_custom_playlist_cover_image
from spotantic.models.playlists.requests import AddCustomPlaylistCoverImageRequest


@pytest.fixture
def file_path() -> Path:
    return Path(__file__).parent / "assets" / "test_playlist_cover.jpg"


@pytest.mark.asyncio
@pytest.mark.mutation
async def test_add_custom_playlist_cover_image(client, playlist_data, file_path):
    result = await add_custom_playlist_cover_image(client, playlist_id=playlist_data.playlist_id, file_path=file_path)

    assert isinstance(result.request, AddCustomPlaylistCoverImageRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
