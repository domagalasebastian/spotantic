from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetShowRequest
from pyspotify.models.spotify import ShowModel


async def get_show(
    client: PySpotifyClient, *, show_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetShowRequest, APIResponse, ShowModel]:
    """Return information about a show.

    Get Spotify catalog information for a single show identified by its unique Spotify ID.

    Args:
        client: PySpotifyClient instance.
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
