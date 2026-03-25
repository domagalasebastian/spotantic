from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.categories.requests import GetSingleBrowseCategoryRequest
from spotantic.models.spotify import CategoryModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyLocaleID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users.")
async def get_single_browse_category(
    client: SpotanticClient, *, category_id: str, locale: Optional[SpotifyLocaleID] = None
) -> APICallModel[GetSingleBrowseCategoryRequest, JsonAPIResponse, CategoryModel]:
    """Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab).

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
    response = await client.request_json(request)
    data = CategoryModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
