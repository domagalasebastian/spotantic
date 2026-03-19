import pytest

from spotantic.endpoints.library import check_user_saved_items
from spotantic.models.library.requests import CheckUserSavedItemsRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_check_user_saved_items(client, example_spotify_uri):
    artist_uri = example_spotify_uri[SpotifyItemType.ARTIST]
    album_uri = example_spotify_uri[SpotifyItemType.ALBUM]

    result = await check_user_saved_items(client, uris=[artist_uri, album_uri])

    assert isinstance(result.request, CheckUserSavedItemsRequest)
    assert isinstance(result.response, list)
    assert all(isinstance(item, bool) for item in result.response)
    assert result.data == {
        artist_uri: result.response[0],
        album_uri: result.response[1],
    }
