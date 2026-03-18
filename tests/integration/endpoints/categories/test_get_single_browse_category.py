import pytest

from spotantic.endpoints.categories import get_single_browse_category
from spotantic.models.categories.requests import GetSingleBrowseCategoryRequest
from spotantic.models.spotify import CategoryModel


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_single_browse_category(client):
    result = await get_single_browse_category(client, category_id="party")

    assert isinstance(result.request, GetSingleBrowseCategoryRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, CategoryModel)
