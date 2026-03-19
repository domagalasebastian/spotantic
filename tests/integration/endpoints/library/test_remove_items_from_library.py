import pytest

from spotantic.endpoints.library import check_user_saved_items
from spotantic.endpoints.library import remove_items_from_library
from spotantic.endpoints.library import save_items_to_library
from spotantic.models.library.requests import RemoveItemsFromLibraryRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def spotify_item_uri(client, example_spotify_uri):
    artist_uri = example_spotify_uri[SpotifyItemType.ARTIST]
    album_uri = example_spotify_uri[SpotifyItemType.ALBUM]

    data = await check_user_saved_items(client, uris=[artist_uri, album_uri])

    yield artist_uri, album_uri

    uris_to_save = [uri for uri, is_saved in data.data.items() if is_saved]

    if uris_to_save:
        await save_items_to_library(client, uris=uris_to_save)


@pytest.mark.asyncio
@pytest.mark.mutation
@pytest.mark.user_library
async def test_remove_items_from_library(client, spotify_item_uri):
    artist_uri, album_uri = spotify_item_uri

    result = await remove_items_from_library(client, uris=[artist_uri, album_uri])

    assert isinstance(result.request, RemoveItemsFromLibraryRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
