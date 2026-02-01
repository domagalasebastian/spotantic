from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.markets.requests import GetAvailableMarketsRequest


async def get_available_markets(
    client: PySpotifyClient,
) -> APICallModel[GetAvailableMarketsRequest, APIResponse, list[SpotifyMarketID]]:
    """Get a list of the markets available to Spotify.

    Get the list of markets where Spotify is available.

    Args:
        client: PySpotifyClient instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAvailableMarketsRequest.build()
    response = await client.request(request)
    assert response is not None
    data = [market for market in response["markets"]]

    return APICallModel(request=request, response=response, data=data)
