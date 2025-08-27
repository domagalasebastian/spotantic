from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import TogglePlaybackShuffleRequest
from pyspotify.models.player.requests import TogglePlaybackShuffleRequestParams


async def toggle_playback_shuffle(
    client: PySpotifyClient, *, state: bool, device_id: Optional[str] = None
) -> APICallModel[TogglePlaybackShuffleRequest, APIResponse, None]:
    request = TogglePlaybackShuffleRequest(
        endpoint="me/player/shuffle",
        params=TogglePlaybackShuffleRequestParams(
            state=state,
            device_id=device_id,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
