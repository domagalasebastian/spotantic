from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import SetRepeatModeRequest
from spotantic.types import APIResponse
from spotantic.types import RepeatMode


async def set_repeat_mode(
    client: SpotanticClient, *, state: RepeatMode, device_id: Optional[str] = None
) -> APICallModel[SetRepeatModeRequest, APIResponse, None]:
    """Set the repeat mode for the user's current playback device.

    Set the repeat mode for the user's playback. This API only works for users who have Spotify Premium.
    The order of execution is not guaranteed when you use this API with other Player API endpoints.

    Args:
        client: SpotanticClient instance.
        state: The repeat mode to set.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SetRepeatModeRequest.build(state=state, device_id=device_id)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
