from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SavedTrackModel
from pyspotify.models.tracks.requests import GetUserSavedTracksRequest
from pyspotify.models.tracks.requests import GetUserSavedTracksRequestParams


async def get_user_saved_tracks(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetUserSavedTracksRequest, APIResponse, PagedResultModel[SavedTrackModel]]:
    request = GetUserSavedTracksRequest(
        endpoint="me/tracks",
        params=GetUserSavedTracksRequestParams(
            limit=limit,
            offset=offset,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SavedTrackModel](**response)

    return APICallModel(request=request, response=response, data=data)
