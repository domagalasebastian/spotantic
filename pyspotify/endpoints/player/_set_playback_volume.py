from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SetPlaybackVolumeRequest
from pyspotify.types import APIResponse


async def set_playback_volume(
    client: PySpotifyClient, *, volume_percent: int, device_id: Optional[str] = None
) -> APICallModel[SetPlaybackVolumeRequest, APIResponse, None]:
    """Set the volume for the user's current playback device.

    Set the volume for the user’s current playback device. This API only works for users
    who have Spotify Premium. The order of execution is not guaranteed when you use this API with
    other Player API endpoints.

    Args:
        client: PySpotifyClient instance.
        volume_percent: The volume to set. Must be a value from 0 to 100 inclusive.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SetPlaybackVolumeRequest.build(volume_percent=volume_percent, device_id=device_id)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
