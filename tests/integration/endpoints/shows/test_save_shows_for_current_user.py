import pytest

from spotantic.endpoints.shows import check_user_saved_shows
from spotantic.endpoints.shows import remove_user_saved_shows
from spotantic.endpoints.shows import save_shows_for_current_user
from spotantic.models.shows.requests import SaveShowsForCurrentUserRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def show_id(client, example_spotify_item_id):
    show_id = example_spotify_item_id[SpotifyItemType.SHOW]
    data = await check_user_saved_shows(client, show_ids=[show_id])
    is_present_in_library = data.data[show_id]

    yield show_id

    if not is_present_in_library:
        await remove_user_saved_shows(client, show_ids=[show_id])


@pytest.mark.asyncio
@pytest.mark.mutation
@pytest.mark.user_library
async def test_save_shows_for_current_user(client, show_id):
    result = await save_shows_for_current_user(client, show_ids=[show_id])

    assert isinstance(result.request, SaveShowsForCurrentUserRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
