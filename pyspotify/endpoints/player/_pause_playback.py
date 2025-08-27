from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import PausePlaybackRequest
from pyspotify.models.player.requests import PausePlaybackRequestParams


async def pause_playback(
    client: PySpotifyClient, *, device_id: Optional[str] = None
) -> APICallModel[PausePlaybackRequest, APIResponse, None]:
    request = PausePlaybackRequest(
        endpoint="me/player/pause",
        params=PausePlaybackRequestParams(
            device_id=device_id,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
