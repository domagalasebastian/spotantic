from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.shows.requests import SaveShowsForCurrentUserRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Save Items to Library instead.")
async def save_shows_for_current_user(
    client: SpotanticClient, *, show_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveShowsForCurrentUserRequest, RawAPIResponse, None]:
    """Save one or more shows to current Spotify user's library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.
       Use *Save Items to Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        show_ids: A list of the Spotify IDs for the shows to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveShowsForCurrentUserRequest.build(show_ids=show_ids)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
