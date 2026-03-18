import pytest

from spotantic.endpoints.episodes import check_user_saved_episodes
from spotantic.endpoints.episodes import remove_user_saved_episodes
from spotantic.endpoints.episodes import save_episodes_for_current_user
from spotantic.models.episodes.requests import RemoveUserSavedEpisodesRequest
from spotantic.types import SpotifyItemType


@pytest.fixture
async def episode_id(client, example_spotify_item_id):
    episode_id = example_spotify_item_id[SpotifyItemType.EPISODE]
    data = await check_user_saved_episodes(client, episode_ids=[episode_id])
    is_present_in_library = data.data[episode_id]

    yield episode_id

    if is_present_in_library:
        await save_episodes_for_current_user(client, episode_ids=[episode_id])


@pytest.mark.asyncio
@pytest.mark.mutation
@pytest.mark.user_library
async def test_remove_user_saved_episodes(client, episode_id):
    result = await remove_user_saved_episodes(client, episode_ids=[episode_id])

    assert isinstance(result.request, RemoveUserSavedEpisodesRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
