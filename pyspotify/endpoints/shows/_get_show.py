from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetShowRequest
from pyspotify.models.shows.requests import GetShowRequestParams
from pyspotify.models.spotify import ShowModel


async def get_show(
    client: PySpotifyClient, *, show_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetShowRequest, APIResponse, ShowModel]:
    request = GetShowRequest(
        endpoint=f"shows/{show_id}",
        params=GetShowRequestParams(
            show_id=show_id,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = ShowModel(**response)

    return APICallModel(request=request, response=response, data=data)
