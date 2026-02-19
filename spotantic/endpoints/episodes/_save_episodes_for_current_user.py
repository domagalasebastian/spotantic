from collections.abc import Sequence

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.episodes.requests import SaveEpisodesForCurrentUserRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Save Items to Library instead.")
async def save_episodes_for_current_user(
    client: SpotanticClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveEpisodesForCurrentUserRequest, APIResponse, None]:
    """Save one or more episodes to the current user's library.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       Use *Save Items to Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        episode_ids: A list of the Spotify IDs for the episodes to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveEpisodesForCurrentUserRequest.build(
        episode_ids=episode_ids,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
