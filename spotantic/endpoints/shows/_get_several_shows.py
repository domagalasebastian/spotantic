from collections.abc import Sequence
from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import GetSeveralShowsRequest
from spotantic.models.spotify import SimplifiedShowModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_several_shows(
    client: SpotanticClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralShowsRequest, APIResponse, list[SimplifiedShowModel]]:
    """Get Spotify catalog information for several shows based on their Spotify IDs.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
