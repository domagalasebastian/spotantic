import pytest

from spotantic.endpoints.users import check_if_user_follows_artists_or_users
from spotantic.models.users.requests import CheckIfUserFollowsArtistsOrUsersRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
@pytest.mark.parametrize("item_type", [SpotifyItemType.ARTIST, SpotifyItemType.USER])
async def test_check_if_user_follows_artists_or_users(client, example_spotify_item_id, item_type):
    item_id = example_spotify_item_id[item_type]
    result = await check_if_user_follows_artists_or_users(
        client,
        item_ids=[item_id],
        item_type=item_type,
    )

    assert isinstance(result.request, CheckIfUserFollowsArtistsOrUsersRequest)
    assert isinstance(result.response, list)
    assert isinstance(result.data, dict)
    assert len(result.data) == 1
    assert isinstance(result.data[item_id], bool)
