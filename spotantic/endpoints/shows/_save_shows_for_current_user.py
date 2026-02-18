from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import SaveShowsForCurrentUserRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def save_shows_for_current_user(
    client: SpotanticClient, *, show_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveShowsForCurrentUserRequest, APIResponse, None]:
    """Save shows to the current Spotify user's library.

    Save one or more shows to current Spotify user's library.

    Args:
        client: SpotanticClient instance.
        show_ids: A list of the Spotify IDs for the shows to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveShowsForCurrentUserRequest.build(show_ids=show_ids)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
