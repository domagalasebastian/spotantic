from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.episodes.requests import SaveEpisodesForCurrentUserRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def save_episodes_for_current_user(
    client: SpotanticClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveEpisodesForCurrentUserRequest, APIResponse, None]:
    """Save episodes to the current Spotify user's library.

    Save one or more episodes to the current user's library.

    Args:
        client: SpotanticClient instance.
        episode_ids: A list of the Spotify IDs for the episodes to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveEpisodesForCurrentUserRequest.build(
        episode_ids=episode_ids,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
