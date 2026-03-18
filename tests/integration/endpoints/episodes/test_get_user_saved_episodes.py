import pytest

from spotantic.endpoints.episodes import get_user_saved_episodes
from spotantic.models.episodes.requests import GetUserSavedEpisodesRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SavedEpisodeModel


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_get_user_saved_episodes(client):
    result = await get_user_saved_episodes(client, limit=50)

    assert isinstance(result.request, GetUserSavedEpisodesRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    if result.data.items:
        assert isinstance(result.data.items[0], SavedEpisodeModel)
