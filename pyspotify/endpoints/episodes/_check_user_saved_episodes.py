from typing import Dict
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.episodes.requests import CheckUserSavedEpisodesRequest
from pyspotify.models.episodes.requests import CheckUserSavedEpisodesRequestParams


async def check_user_saved_episodes(
    client: PySpotifyClient, *, episode_ids: Sequence[SpotifyItemID]
) -> APICallModel[CheckUserSavedEpisodesRequest, APIResponse, Dict[SpotifyItemID, bool]]:
    request = CheckUserSavedEpisodesRequest(
        endpoint="me/episodes/contains",
        params=CheckUserSavedEpisodesRequestParams(
            episode_ids=episode_ids,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = dict(zip(episode_ids, response))

    return APICallModel(request=request, response=response, data=data)
