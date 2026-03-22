import pytest

from spotantic.endpoints.users import check_if_current_user_follows_playlist
from spotantic.endpoints.users import follow_playlist
from spotantic.endpoints.users import unfollow_playlist
from spotantic.models.users.requests import UnfollowPlaylistRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def playlist_id(client, example_spotify_item_id):
    item_id = example_spotify_item_id[SpotifyItemType.PLAYLIST]
    data = await check_if_current_user_follows_playlist(client, playlist_id=item_id)
    is_present_in_library = data.data

    yield item_id

    if is_present_in_library:
        await follow_playlist(client, playlist_id=item_id)


@pytest.mark.asyncio
@pytest.mark.mutation
@pytest.mark.user_library
async def test_unfollow_playlist(client, playlist_id):
    result = await unfollow_playlist(client, playlist_id=playlist_id)

    assert isinstance(result.request, UnfollowPlaylistRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
