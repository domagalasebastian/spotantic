from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import GetUserSavedEpisodesRequest
from pyspotify.models.episodes.requests import GetUserSavedEpisodesRequestParams
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SavedEpisodeModel


async def get_user_saved_episodes(
    client: PySpotifyClient, *, limit: int = 20, offset: int = 0, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetUserSavedEpisodesRequest, APIResponse, PagedResultModel[SavedEpisodeModel]]:
    request = GetUserSavedEpisodesRequest(
        endpoint="me/episodes",
        params=GetUserSavedEpisodesRequestParams(
            limit=limit,
            offset=offset,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SavedEpisodeModel](**response)

    return APICallModel(request=request, response=response, data=data)
