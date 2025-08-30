from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetUserSavedShowsRequest
from pyspotify.models.shows.requests import GetUserSavedShowsRequestParams
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SavedShowModel


async def get_user_saved_shows(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0
) -> APICallModel[GetUserSavedShowsRequest, APIResponse, PagedResultModel[SavedShowModel]]:
    request = GetUserSavedShowsRequest(
        endpoint="me/shows",
        params=GetUserSavedShowsRequestParams(
            limit=limit,
            offset=offset,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SavedShowModel](**response)

    return APICallModel(request=request, response=response, data=data)
