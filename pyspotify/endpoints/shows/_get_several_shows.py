from typing import List
from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import GetSeveralShowsRequest
from pyspotify.models.spotify import SimplifiedShowModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_several_shows(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralShowsRequest, APIResponse, List[SimplifiedShowModel]]:
    """Return information about several shows at the time.

    Get Spotify catalog information for several shows based on their Spotify IDs.

    Args:
        client: PySpotifyClient instance.
        show_ids: A list of the Spotify IDs for the shows.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralShowsRequest.build(show_ids=show_ids, market=market)
    response = await client.request(request)
    assert response is not None
    data = [SimplifiedShowModel(**show_data) for show_data in response["shows"]]

    return APICallModel(request=request, response=response, data=data)
