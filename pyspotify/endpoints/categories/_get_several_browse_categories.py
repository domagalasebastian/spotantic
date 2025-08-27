from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyLocaleID
from pyspotify.models import APICallModel
from pyspotify.models.categories.requests import GetSeveralBrowseCategoriesRequest
from pyspotify.models.categories.requests import GetSeveralBrowseCategoriesRequestParams
from pyspotify.models.spotify import CategoryModel
from pyspotify.models.spotify import PagedResultModel


async def get_several_browse_categories(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0, locale: Optional[SpotifyLocaleID] = None
) -> APICallModel[GetSeveralBrowseCategoriesRequest, APIResponse, PagedResultModel[CategoryModel]]:
    request = GetSeveralBrowseCategoriesRequest(
        endpoint="browse/categories",
        params=GetSeveralBrowseCategoriesRequestParams(
            limit=limit,
            offset=offset,
            locale=locale,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[CategoryModel](**response["categories"])

    return APICallModel(request=request, response=response, data=data)
