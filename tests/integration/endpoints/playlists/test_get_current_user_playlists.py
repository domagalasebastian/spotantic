import pytest

from spotantic.endpoints.playlists import get_current_user_playlist
from spotantic.models.playlists.requests import GetCurrentUserPlaylistsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedPlaylistModel


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_get_current_user_playlists(client):
    result = await get_current_user_playlist(client, limit=50)

    assert isinstance(result.request, GetCurrentUserPlaylistsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, SimplifiedPlaylistModel) for item in result.data.items)
