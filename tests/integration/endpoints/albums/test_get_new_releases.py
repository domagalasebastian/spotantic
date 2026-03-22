import pytest

from spotantic.endpoints.albums import get_new_releases
from spotantic.models.albums.requests import GetNewReleasesRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedAlbumModel


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_new_releases(client):
    result = await get_new_releases(client, limit=50)

    assert isinstance(result.request, GetNewReleasesRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, SimplifiedAlbumModel) for item in result.data.items)
