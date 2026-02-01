from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import RepeatMode
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SetRepeatModeRequest


async def set_repeat_mode(
    client: PySpotifyClient, *, state: RepeatMode, device_id: Optional[str] = None
) -> APICallModel[SetRepeatModeRequest, APIResponse, None]:
    """Set the repeat mode for the user's current playback device.

    Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium.
    The order of execution is not guaranteed when you use this API with other Player API endpoints.

    Args:
        client: PySpotifyClient instance.
        state: The repeat mode to set.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SetRepeatModeRequest.build(state=state, device_id=device_id)
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
