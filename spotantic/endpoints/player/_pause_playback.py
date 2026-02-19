from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import PausePlaybackRequest
from spotantic.types import APIResponse


async def pause_playback(
    client: SpotanticClient, *, device_id: Optional[str] = None
) -> APICallModel[PausePlaybackRequest, APIResponse, None]:
    """Pause playback on the user's account.

    Pause playback on the user's account. This API only works for users who have Spotify Premium.
    The order of execution is not guaranteed when you use this API with other Player API endpoints.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = PausePlaybackRequest.build(device_id=device_id)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
