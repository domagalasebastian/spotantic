from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import RemoveUserSavedEpisodesRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def remove_user_saved_episodes(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedEpisodesRequest, APIResponse, None]:
    """Remove episodes from the current Spotify user's library.

    Remove one or more episodes from the current user's library.

    Args:
        client: PySpotifyClient instance.
        episode_ids: A list of Spotify IDs for the episodes to be removed from the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = RemoveUserSavedEpisodesRequest.build(
        episode_ids=episode_ids,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
