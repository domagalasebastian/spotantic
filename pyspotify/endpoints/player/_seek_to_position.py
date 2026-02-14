from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SeekToPositionRequest
from pyspotify.types import APIResponse


async def seek_to_position(
    client: PySpotifyClient, *, position_ms: int, device_id: Optional[str] = None
) -> APICallModel[SeekToPositionRequest, APIResponse, None]:
    """Seek to position in currently playing track.

    Seeks to the given position in the user’s currently playing track. This API only works for users
    who have Spotify Premium. The order of execution is not guaranteed when you use this API with
    other Player API endpoints.

    Args:
        client: PySpotifyClient instance.
        position_ms: The position in milliseconds to seek to.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SeekToPositionRequest.build(position_ms=position_ms, device_id=device_id)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
