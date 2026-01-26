from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.shows.requests import SaveShowsForCurrentUserRequest


async def save_shows_for_current_user(
    client: PySpotifyClient, *, show_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveShowsForCurrentUserRequest, APIResponse, None]:
    """Save shows to the current Spotify user's library.

    Save one or more shows to current Spotify user's library.

    Args:
        client: PySpotifyClient instance.
        show_ids: A list of the Spotify IDs for the shows to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveShowsForCurrentUserRequest.build(show_ids=show_ids)
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
