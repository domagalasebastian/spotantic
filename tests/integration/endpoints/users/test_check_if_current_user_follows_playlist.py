import pytest

from spotantic.endpoints.users import check_if_current_user_follows_playlist
from spotantic.models.users.requests import CheckIfCurrentUserFollowsPlaylistRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_check_if_current_user_follows_playlist(client, example_spotify_item_id):
    result = await check_if_current_user_follows_playlist(
        client,
        playlist_id=example_spotify_item_id[SpotifyItemType.PLAYLIST],
    )

    assert isinstance(result.request, CheckIfCurrentUserFollowsPlaylistRequest)
    assert isinstance(result.response, list)
    assert isinstance(result.data, bool)
