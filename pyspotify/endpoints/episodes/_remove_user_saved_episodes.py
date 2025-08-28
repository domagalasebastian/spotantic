from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import RemoveUserSavedEpisodesRequest
from pyspotify.models.episodes.requests import RemoveUserSavedEpisodesRequestParams


async def remove_user_saved_episodes(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[RemoveUserSavedEpisodesRequest, APIResponse, None]:
    request = RemoveUserSavedEpisodesRequest(
        endpoint="me/episodes",
        params=RemoveUserSavedEpisodesRequestParams(
            episode_ids=episode_ids,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
