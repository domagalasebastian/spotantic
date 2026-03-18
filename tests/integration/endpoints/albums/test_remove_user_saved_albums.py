import pytest

from spotantic.endpoints.albums import check_user_saved_albums
from spotantic.endpoints.albums import remove_user_saved_albums
from spotantic.endpoints.albums import save_albums_for_current_user
from spotantic.models.albums.requests import RemoveUserSavedAlbumsRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def album_id(client, example_spotify_item_id):
    album_id = example_spotify_item_id[SpotifyItemType.ALBUM]
    data = await check_user_saved_albums(client, album_ids=[album_id])
    is_present_in_library = data.data[album_id]

    yield album_id

    if is_present_in_library:
        await save_albums_for_current_user(client, album_ids=[album_id])


@pytest.mark.asyncio
@pytest.mark.mutation
@pytest.mark.user_library
async def test_remove_user_saved_albums(client, album_id):
    result = await remove_user_saved_albums(client, album_ids=[album_id])

    assert isinstance(result.request, RemoveUserSavedAlbumsRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
