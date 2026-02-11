from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import CheckUserSavedEpisodesRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def check_user_saved_episodes(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedEpisodesRequest, APIResponse, dict[SpotifyItemID, bool]]:
    """Check if episodes are saved in the user's library.

    Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.

    Args:
        client: PySpotifyClient instance.
        episode_ids: A list of Spotify IDs for the episodes to check.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckUserSavedEpisodesRequest.build(episode_ids=episode_ids)
    response = await client.request(request)
    assert response is not None
    data = dict(zip(episode_ids, response))

    return APICallModel(request=request, response=response, data=data)
