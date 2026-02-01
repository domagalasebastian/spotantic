from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SkipToPreviousRequest


async def skip_to_previous(
    client: PySpotifyClient, *, device_id: Optional[str] = None
) -> APICallModel[SkipToPreviousRequest, APIResponse, None]:
    """Skip to previous track in the user's queue.

    Skips to previous track in the user’s queue. This API only works for users who have Spotify Premium.
    The order of execution is not guaranteed when you use this API with other Player API endpoints.

    Args:
        client: PySpotifyClient instance.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SkipToPreviousRequest.build(
        device_id=device_id,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
