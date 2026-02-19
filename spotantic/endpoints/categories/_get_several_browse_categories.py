from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.categories.requests import GetSeveralBrowseCategoriesRequest
from spotantic.models.spotify import CategoryModel
from spotantic.models.spotify import PagedResultModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyLocaleID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_several_browse_categories(
    client: SpotanticClient, *, limit: int = 20, offset: int = 0, locale: Optional[SpotifyLocaleID] = None
) -> APICallModel[GetSeveralBrowseCategoriesRequest, APIResponse, PagedResultModel[CategoryModel]]:
    """Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
