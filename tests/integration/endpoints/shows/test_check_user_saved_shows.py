import pytest

from spotantic.endpoints.shows import check_user_saved_shows
from spotantic.models.shows.requests import CheckUserSavedShowsRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_check_user_saved_shows(client, example_spotify_item_id):
    show_id = example_spotify_item_id[SpotifyItemType.SHOW]
    result = await check_user_saved_shows(client, show_ids=[show_id])

    assert isinstance(result.request, CheckUserSavedShowsRequest)
    assert isinstance(result.response, list)
    assert isinstance(result.data, dict)
    assert len(result.data) == 1
    assert isinstance(result.data[show_id], bool)
