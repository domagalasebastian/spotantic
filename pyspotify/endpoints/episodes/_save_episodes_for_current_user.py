from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import SaveEpisodesForCurrentUserRequest
from pyspotify.models.episodes.requests import SaveEpisodesForCurrentUserRequestParams


async def save_episodes_for_current_user(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[SaveEpisodesForCurrentUserRequest, APIResponse, None]:
    request = SaveEpisodesForCurrentUserRequest(
        endpoint="me/episodes",
        params=SaveEpisodesForCurrentUserRequestParams(
            episode_ids=episode_ids,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
