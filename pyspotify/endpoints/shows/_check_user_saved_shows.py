from typing import Dict
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import CheckUserSavedShowsRequest
from pyspotify.models.shows.requests import CheckUserSavedShowsRequestParams


async def check_user_saved_shows(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedShowsRequest, APIResponse, Dict[SpotifyItemID, bool]]:
    request = CheckUserSavedShowsRequest(
        endpoint="me/shows/contains",
        params=CheckUserSavedShowsRequestParams(
            show_ids=show_ids,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(show_ids, response))

    return APICallModel(request=request, response=response, data=data)
