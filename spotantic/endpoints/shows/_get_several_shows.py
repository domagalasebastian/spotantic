from typing import List
from typing import Optional
from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import GetSeveralShowsRequest
from spotantic.models.spotify import SimplifiedShowModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_several_shows(
    client: SpotanticClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralShowsRequest, APIResponse, List[SimplifiedShowModel]]:
    """Return information about several shows at the time.

    Get Spotify catalog information for several shows based on their Spotify IDs.

    Args:
        client: SpotanticClient instance.
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
