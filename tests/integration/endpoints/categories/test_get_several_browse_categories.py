import pytest

from spotantic.endpoints.categories import get_several_browse_categories
from spotantic.models.categories.requests import GetSeveralBrowseCategoriesRequest
from spotantic.models.spotify import CategoryModel
from spotantic.models.spotify import PagedResultModel


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_several_browse_categories(client):
    result = await get_several_browse_categories(client, limit=50)

    assert isinstance(result.request, GetSeveralBrowseCategoriesRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, PagedResultModel)
    assert all(isinstance(item, CategoryModel) for item in result.data.items)
