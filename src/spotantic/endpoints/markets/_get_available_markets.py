from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.markets.requests import GetAvailableMarketsRequest
from spotantic.models.markets.responses import GetAvailableMarketsResponse
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users.")
async def get_available_markets(
    client: SpotanticClient,
) -> APICallModel[GetAvailableMarketsRequest, JsonAPIResponse, list[SpotifyMarketID]]:
    """Get the list of markets where Spotify is available.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAvailableMarketsRequest.build()
    response = await client.request_json(request)
    data = GetAvailableMarketsResponse.model_validate(response)

    return APICallModel(request=request, response=response, data=data.markets)
