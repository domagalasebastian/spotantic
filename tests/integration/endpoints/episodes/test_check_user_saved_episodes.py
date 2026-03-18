import pytest

from spotantic.endpoints.episodes import check_user_saved_episodes
from spotantic.models.episodes.requests import CheckUserSavedEpisodesRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_check_user_saved_episodes(client, example_spotify_item_id):
    episode_id = example_spotify_item_id[SpotifyItemType.EPISODE]

    result = await check_user_saved_episodes(client, episode_ids=[episode_id])

    assert isinstance(result.request, CheckUserSavedEpisodesRequest)
    assert isinstance(result.response, list)
    assert isinstance(result.data, dict)
    assert len(result.data) == 1
    assert isinstance(result.data[episode_id], bool)
