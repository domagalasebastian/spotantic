import pytest

from spotantic.endpoints.albums import get_user_saved_albums
from spotantic.models.albums.requests import GetUserSavedAlbumsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SavedAlbumModel


@pytest.mark.asyncio
@pytest.mark.readonly
@pytest.mark.user_library
async def test_get_user_saved_albums(client):
    result = await get_user_saved_albums(client, limit=50)

    assert isinstance(result.request, GetUserSavedAlbumsRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    if result.data.items:
        assert isinstance(result.data.items[0], SavedAlbumModel)
