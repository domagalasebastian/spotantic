from typing import List
from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetSeveralShowsRequest
from pyspotify.models.shows.requests import GetSeveralShowsRequestParams
from pyspotify.models.spotify import SimplifiedShowModel


async def get_several_shows(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralShowsRequest, APIResponse, List[SimplifiedShowModel]]:
    request = GetSeveralShowsRequest(
        endpoint="shows",
        params=GetSeveralShowsRequestParams(
            show_ids=show_ids,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = [SimplifiedShowModel(**show_data) for show_data in response["shows"]]

    return APICallModel(request=request, response=response, data=data)
