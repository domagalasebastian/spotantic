from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import GetShowRequest
from spotantic.models.spotify import ShowModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_show(
    client: SpotanticClient, *, show_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetShowRequest, APIResponse, ShowModel]:
    """Return information about a show.

    Get Spotify catalog information for a single show identified by its unique Spotify ID.

    Args:
        client: SpotanticClient instance.
        show_id: The Spotify ID for the show.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetShowRequest.build(show_id=show_id, market=market)
    response = await client.request(request)
    assert response is not None
    data = ShowModel(**response)

    return APICallModel(request=request, response=response, data=data)
