from collections.abc import Sequence
from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import GetSeveralShowsRequest
from spotantic.models.shows.responses import GetSeveralShowsResponse
from spotantic.models.spotify import SimplifiedShowModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated since 11 February 2026 for new users.")
async def get_several_shows(
    client: SpotanticClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralShowsRequest, JsonAPIResponse, list[SimplifiedShowModel]]:
    """Get Spotify catalog information for several shows based on their Spotify IDs.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        show_ids: A list of the Spotify IDs for the shows.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralShowsRequest.build(show_ids=show_ids, market=market)
    response = await client.request_json(request)
    data = GetSeveralShowsResponse.model_validate(response)

    return APICallModel(request=request, response=response, data=data.shows)
