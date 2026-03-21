import pytest

from spotantic.endpoints.shows import get_user_saved_shows
from spotantic.models.shows.requests import GetUserSavedShowsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SavedShowModel


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_get_user_saved_shows(client):
    result = await get_user_saved_shows(client, limit=50)

    assert isinstance(result.request, GetUserSavedShowsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, SavedShowModel) for item in result.data.items)
