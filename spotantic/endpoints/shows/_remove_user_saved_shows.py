from collections.abc import Sequence
from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import RemoveUserSavedShowsRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


@deprecated("This endpoint is deprecated. Use Remove Items from Library instead.")
async def remove_user_saved_shows(
    client: SpotanticClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[RemoveUserSavedShowsRequest, RawAPIResponse, None]:
    """Delete one or more shows from current Spotify user's library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       Use *Remove Items from Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        show_ids: A list of the Spotify IDs for the shows to be removed from the user's library.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveUserSavedShowsRequest.build(show_ids=show_ids, market=market)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
