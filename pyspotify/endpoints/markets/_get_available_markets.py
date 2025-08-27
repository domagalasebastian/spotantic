from typing import List

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.markets.requests import GetAvailableMarketsRequest


async def get_available_markets(
    client: PySpotifyClient,
) -> APICallModel[GetAvailableMarketsRequest, APIResponse, List[SpotifyMarketID]]:
    request = GetAvailableMarketsRequest(
        endpoint="markets",
    )
    response = await client.request(request)
    assert response is not None
    data = [market for market in response["markets"]]

    return APICallModel(request=request, response=response, data=data)
