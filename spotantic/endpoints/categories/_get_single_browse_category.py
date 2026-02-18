from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.categories.requests import GetSingleBrowseCategoryRequest
from spotantic.models.spotify import CategoryModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyLocaleID


async def get_single_browse_category(
    client: SpotanticClient, *, category_id: str, locale: Optional[SpotifyLocaleID] = None
) -> APICallModel[GetSingleBrowseCategoryRequest, APIResponse, CategoryModel]:
    """Get Spotify catalog information for a single browse category.

    Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

    Args:
        client: SpotanticClient instance.
        category_id: The Spotify ID for the browse category.
        locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code,
         joined by an underscore.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSingleBrowseCategoryRequest.build(
        category_id=category_id,
        locale=locale,
    )
    response = await client.request(request)
    assert response is not None
    data = CategoryModel(**response)

    return APICallModel(request=request, response=response, data=data)
