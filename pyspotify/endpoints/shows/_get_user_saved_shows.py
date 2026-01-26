from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetUserSavedShowsRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SavedShowModel


async def get_user_saved_shows(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0
) -> APICallModel[GetUserSavedShowsRequest, APIResponse, PagedResultModel[SavedShowModel]]:
    """Return a list of the shows saved in the current Spotify user's library.

    Get a list of shows saved in the current Spotify user's library.
    Optional parameters can be used to limit the number of shows returned.

    Args:
        client: PySpotifyClient instance.
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
