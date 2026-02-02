from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyLocaleID
from pyspotify.models import APICallModel
from pyspotify.models.categories.requests import GetSeveralBrowseCategoriesRequest
from pyspotify.models.spotify import CategoryModel
from pyspotify.models.spotify import PagedResultModel


async def get_several_browse_categories(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0, locale: Optional[SpotifyLocaleID] = None
) -> APICallModel[GetSeveralBrowseCategoriesRequest, APIResponse, PagedResultModel[CategoryModel]]:
    """Get Spotify catalog information for several browse categories.

    Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

    Args:
        client: PySpotifyClient instance.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.
        locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code,
         joined by an underscore.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralBrowseCategoriesRequest.build(
        limit=limit,
        offset=offset,
        locale=locale,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[CategoryModel](**response["categories"])

    return APICallModel(request=request, response=response, data=data)
