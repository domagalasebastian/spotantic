import pytest

from spotantic.endpoints.users import check_if_user_follows_artists_or_users
from spotantic.endpoints.users import follow_artists_or_users
from spotantic.endpoints.users import unfollow_artists_or_users
from spotantic.models.users.requests import UnfollowArtistsOrUsersRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def item_data(request, client, example_spotify_item_id):
    item_type = request.param
    item_id = example_spotify_item_id[item_type]
    data = await check_if_user_follows_artists_or_users(client, item_ids=[item_id], item_type=item_type)
    is_present_in_library = data.data[item_id]

    yield item_type, item_id

    if is_present_in_library:
        await follow_artists_or_users(client, item_ids=[item_id], item_type=item_type)


@pytest.mark.asyncio
@pytest.mark.mutation
@pytest.mark.user_library
@pytest.mark.parametrize("item_data", [SpotifyItemType.ARTIST, SpotifyItemType.USER], indirect=True)
async def test_unfollow_artists_or_users(client, item_data):
    item_type, item_id = item_data
    result = await unfollow_artists_or_users(
        client,
        item_ids=[item_id],
        item_type=item_type,
    )

    assert isinstance(result.request, UnfollowArtistsOrUsersRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
