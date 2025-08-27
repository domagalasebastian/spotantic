from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyLocaleID
from pyspotify.models import APICallModel
from pyspotify.models.categories.requests import GetSingleBrowseCategoryRequest
from pyspotify.models.categories.requests import GetSingleBrowseCategoryRequestParams
from pyspotify.models.spotify import CategoryModel


async def get_single_browse_category(
    client: PySpotifyClient, *, category_id: str, locale: Optional[SpotifyLocaleID] = None
) -> APICallModel[GetSingleBrowseCategoryRequest, APIResponse, CategoryModel]:
    request = GetSingleBrowseCategoryRequest(
        endpoint=f"browse/categories/{category_id}",
        params=GetSingleBrowseCategoryRequestParams(
            category_id=category_id,
            locale=locale,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = CategoryModel(**response)

    return APICallModel(request=request, response=response, data=data)
