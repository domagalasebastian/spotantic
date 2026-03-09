from typing_extensions import deprecated

from spotantic._utils.models._type_validation import validate_is_instance_of
from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.markets.requests import GetAvailableMarketsRequest
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_available_markets(
    client: SpotanticClient,
) -> APICallModel[GetAvailableMarketsRequest, JsonAPIResponse, list[SpotifyMarketID]]:
    """Get the list of markets where Spotify is available.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAvailableMarketsRequest.build()
    response = await client.request_json(request)
    data = validate_is_instance_of(response, list[SpotifyMarketID])

    return APICallModel(request=request, response=response, data=data)
