from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import TogglePlaybackShuffleRequest
from pyspotify.types import APIResponse


async def toggle_playback_shuffle(
    client: PySpotifyClient, *, state: bool, device_id: Optional[str] = None
) -> APICallModel[TogglePlaybackShuffleRequest, APIResponse, None]:
    """Toggle shuffle state for user's playback.

    Toggle shuffle on or off for user’s playback. This API only works for users who have Spotify Premium.
    The order of execution is not guaranteed when you use this API with other Player API endpoints.

    Args:
        client: PySpotifyClient instance.
        state: True to turn shuffle on, false to turn it off.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = TogglePlaybackShuffleRequest.build(state=state, device_id=device_id)
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
