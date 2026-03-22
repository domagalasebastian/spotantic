import pytest

from spotantic.endpoints.tracks import get_user_saved_tracks
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SavedTrackModel
from spotantic.models.tracks.requests import GetUserSavedTracksRequest


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_get_user_saved_tracks(client):
    result = await get_user_saved_tracks(client, limit=50)

    assert isinstance(result.request, GetUserSavedTracksRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, SavedTrackModel) for item in result.data.items)
