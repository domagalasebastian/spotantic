from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import GetUserSavedShowsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SavedShowModel
from spotantic.types import APIResponse


async def get_user_saved_shows(
    client: SpotanticClient, *, limit: int = 20, offset: int = 0
) -> APICallModel[GetUserSavedShowsRequest, APIResponse, PagedResultModel[SavedShowModel]]:
    """Return a list of the shows saved in the current Spotify user's library.

    Get a list of shows saved in the current Spotify user's library.
    Optional parameters can be used to limit the number of shows returned.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
        offset: The index of the first item to return. Default: 0 (the first item).
          Use with limit to get the next set of items.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserSavedShowsRequest.build(
        limit=limit,
        offset=offset,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SavedShowModel](**response)

    return APICallModel(request=request, response=response, data=data)
