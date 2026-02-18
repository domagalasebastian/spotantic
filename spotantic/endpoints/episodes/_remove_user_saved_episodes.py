from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.episodes.requests import RemoveUserSavedEpisodesRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def remove_user_saved_episodes(
    client: SpotanticClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedEpisodesRequest, APIResponse, None]:
    """Remove episodes from the current Spotify user's library.

    Remove one or more episodes from the current user's library.

    Args:
        client: SpotanticClient instance.
        episode_ids: A list of Spotify IDs for the episodes to be removed from the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveUserSavedEpisodesRequest.build(
        episode_ids=episode_ids,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
