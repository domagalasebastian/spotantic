from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyLocaleID
from pyspotify.models import APICallModel
from pyspotify.models.categories.requests import GetSingleBrowseCategoryRequest
from pyspotify.models.spotify import CategoryModel


async def get_single_browse_category(
    client: PySpotifyClient, *, category_id: str, locale: Optional[SpotifyLocaleID] = None
) -> APICallModel[GetSingleBrowseCategoryRequest, APIResponse, CategoryModel]:
    """Get Spotify catalog information for a single browse category.

    Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

    Args:
        client: PySpotifyClient instance.
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
