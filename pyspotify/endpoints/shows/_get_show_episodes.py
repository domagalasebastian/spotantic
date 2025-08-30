from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetShowEpisodesRequest
from pyspotify.models.shows.requests import GetShowEpisodesRequestParams
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedEpisodeModel


async def get_show_episodes(
    client: PySpotifyClient,
    *,
    show_id: SpotifyItemID,
    limit: int = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetShowEpisodesRequest, APIResponse, PagedResultModel[SimplifiedEpisodeModel]]:
    request = GetShowEpisodesRequest(
        endpoint=f"shows/{show_id}/episodes",
        params=GetShowEpisodesRequestParams(
            show_id=show_id,
            limit=limit,
            offset=offset,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedEpisodeModel](**response)

    return APICallModel(request=request, response=response, data=data)
