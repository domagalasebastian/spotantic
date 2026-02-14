from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import RemoveUserSavedShowsRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def remove_user_saved_shows(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[RemoveUserSavedShowsRequest, APIResponse, None]:
    """Remove shows from the current Spotify user's library.

    Delete one or more shows from current Spotify user's library.

    Args:
        client: PySpotifyClient instance.
        show_ids: A list of the Spotify IDs for the shows to be removed from the user's library.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveUserSavedShowsRequest.build(show_ids=show_ids, market=market)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
