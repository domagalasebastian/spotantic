from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.markets.requests import GetAvailableMarketsRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyMarketID


async def get_available_markets(
    client: SpotanticClient,
) -> APICallModel[GetAvailableMarketsRequest, APIResponse, list[SpotifyMarketID]]:
    """Get a list of the markets available to Spotify.

    Get the list of markets where Spotify is available.

    Args:
        client: SpotanticClient instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAvailableMarketsRequest.build()
    response = await client.request(request)
    assert response is not None
    data = [market for market in response["markets"]]

    return APICallModel(request=request, response=response, data=data)
