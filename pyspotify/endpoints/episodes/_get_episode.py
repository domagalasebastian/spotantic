from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import GetEpisodeRequest
from pyspotify.models.episodes.requests import GetEpisodeRequestParams
from pyspotify.models.spotify import EpisodeModel


async def get_episode(
    client: PySpotifyClient, *, episode_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetEpisodeRequest, APIResponse, EpisodeModel]:
    request = GetEpisodeRequest(
        endpoint=f"episodes/{episode_id}",
        params=GetEpisodeRequestParams(
            episode_id=episode_id,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = EpisodeModel(**response)

    return APICallModel(request=request, response=response, data=data)
