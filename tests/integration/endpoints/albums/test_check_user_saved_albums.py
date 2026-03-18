import pytest

from spotantic.endpoints.albums import check_user_saved_albums
from spotantic.models.albums.requests import CheckUserSavedAlbumsRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_check_user_saved_albums(client, example_spotify_item_id):
    album_id = example_spotify_item_id[SpotifyItemType.ALBUM]

    result = await check_user_saved_albums(client, album_ids=[album_id])

    assert isinstance(result.request, CheckUserSavedAlbumsRequest)
    assert isinstance(result.response, list)
    assert isinstance(result.data, dict)
    assert len(result.data) == 1
    assert isinstance(result.data[album_id], bool)
