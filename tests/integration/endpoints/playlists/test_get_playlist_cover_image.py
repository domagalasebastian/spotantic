import pytest

from spotantic.endpoints.playlists import get_playlist_cover_image
from spotantic.models.playlists.requests import GetPlaylistCoverImageRequest
from spotantic.models.spotify import ImageModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_playlist_cover_image(client, example_spotify_item_id):
    result = await get_playlist_cover_image(client, playlist_id=example_spotify_item_id[SpotifyItemType.PLAYLIST])

    assert isinstance(result.request, GetPlaylistCoverImageRequest)
    assert isinstance(result.response, list)
    assert all(isinstance(item, ImageModel) for item in result.data)
