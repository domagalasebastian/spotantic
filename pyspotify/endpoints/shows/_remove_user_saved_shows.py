from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import RemoveUserSavedShowsRequest
from pyspotify.models.shows.requests import RemoveUserSavedShowsRequestParams


async def remove_user_saved_shows(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[RemoveUserSavedShowsRequest, APIResponse, None]:
    request = RemoveUserSavedShowsRequest(
        endpoint="me/shows",
        params=RemoveUserSavedShowsRequestParams(
            show_ids=show_ids,
            market=market,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
