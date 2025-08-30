from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import SaveShowsForCurrentUserRequest
from pyspotify.models.shows.requests import SaveShowsForCurrentUserRequestParams


async def save_shows_for_current_user(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveShowsForCurrentUserRequest, APIResponse, None]:
    request = SaveShowsForCurrentUserRequest(
        endpoint="me/shows",
        params=SaveShowsForCurrentUserRequestParams(
            show_ids=show_ids,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
