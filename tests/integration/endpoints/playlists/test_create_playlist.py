import pytest

from spotantic.endpoints.library import remove_items_from_library
from spotantic.endpoints.playlists import create_playlist
from spotantic.models.playlists.requests import CreatePlaylistRequest
from spotantic.models.spotify import PlaylistModel


@pytest.mark.asyncio
@pytest.mark.mutation
async def test_create_playlist(client):
    result = await create_playlist(client, name="Test Playlist", public=False)

    try:
        assert isinstance(result.request, CreatePlaylistRequest)
        assert isinstance(result.response, dict)
        assert isinstance(result.data, PlaylistModel)
    except AssertionError:
        raise
    finally:
        await remove_items_from_library(client, uris=[result.data.playlist_uri])
