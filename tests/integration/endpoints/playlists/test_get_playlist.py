import pytest

from spotantic.endpoints.playlists import get_playlist
from spotantic.models.playlists.requests import GetPlaylistRequest
from spotantic.models.spotify import PlaylistModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_playlist(client, example_spotify_item_id):
    result = await get_playlist(client, playlist_id=example_spotify_item_id[SpotifyItemType.PLAYLIST])

    assert isinstance(result.request, GetPlaylistRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PlaylistModel)
