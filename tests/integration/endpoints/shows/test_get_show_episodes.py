import pytest

from spotantic.endpoints.shows import get_show_episodes
from spotantic.models.shows.requests import GetShowEpisodesRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedEpisodeModel
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_show_episodes(client, example_spotify_item_id):
    show_id = example_spotify_item_id[SpotifyItemType.SHOW]
    result = await get_show_episodes(client, show_id=show_id, limit=50)

    assert isinstance(result.request, GetShowEpisodesRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, SimplifiedEpisodeModel) for item in result.data.items)
