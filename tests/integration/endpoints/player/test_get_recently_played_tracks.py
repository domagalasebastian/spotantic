import pytest

from spotantic.endpoints.player import get_recently_played_tracks
from spotantic.models.player.requests import GetRecentlyPlayedTracksRequest
from spotantic.models.spotify import PagedResultWithCursorsModel
from spotantic.models.spotify import PlayHistoryModel


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_recently_played_tracks(client):
    result = await get_recently_played_tracks(client, limit=50)

    assert isinstance(result.request, GetRecentlyPlayedTracksRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultWithCursorsModel)
    assert all(isinstance(item, PlayHistoryModel) for item in result.data.items)
