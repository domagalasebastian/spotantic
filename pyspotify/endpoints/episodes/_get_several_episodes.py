from typing import List
from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import GetSeveralEpisodesRequest
from pyspotify.models.episodes.requests import GetSeveralEpisodesRequestParams
from pyspotify.models.spotify import EpisodeModel


async def get_several_episodes(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralEpisodesRequest, APIResponse, List[EpisodeModel]]:
    request = GetSeveralEpisodesRequest(
        endpoint="episodes",
        params=GetSeveralEpisodesRequestParams(
            episode_ids=episode_ids,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = [EpisodeModel(**episode_data) for episode_data in response["episodes"]]

    return APICallModel(request=request, response=response, data=data)
