import pytest

from spotantic.endpoints.episodes import get_several_episodes
from spotantic.models.episodes.requests import GetSeveralEpisodesRequest
from spotantic.models.spotify import EpisodeModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_several_episodes(client, example_spotify_item_id):
    episode_id = example_spotify_item_id[SpotifyItemType.EPISODE]

    result = await get_several_episodes(client, episode_ids=[episode_id])

    assert isinstance(result.request, GetSeveralEpisodesRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
    assert len(result.data) == 1
    assert isinstance(result.data[0], EpisodeModel)
