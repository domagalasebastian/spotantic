from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import SaveEpisodesForCurrentUserRequest


async def save_episodes_for_current_user(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveEpisodesForCurrentUserRequest, APIResponse, None]:
    """Save episodes to the current Spotify user's library.

    Save one or more episodes to the current user's library.

    Args:
        client: PySpotifyClient instance.
        episode_ids: A list of the Spotify IDs for the episodes to be saved to the user's library.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SaveEpisodesForCurrentUserRequest.build(
        episode_ids=episode_ids,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
