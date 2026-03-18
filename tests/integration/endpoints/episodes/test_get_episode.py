import pytest

from spotantic.endpoints.episodes import get_episode
from spotantic.models.episodes.requests import GetEpisodeRequest
from spotantic.models.spotify import EpisodeModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_episode(client, example_spotify_item_id):
    episode_id = example_spotify_item_id[SpotifyItemType.EPISODE]

    result = await get_episode(client, episode_id=episode_id)

    assert isinstance(result.request, GetEpisodeRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, EpisodeModel)
