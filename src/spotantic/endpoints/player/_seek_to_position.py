from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import SeekToPositionRequest
from spotantic.types import RawAPIResponse


async def seek_to_position(
    client: SpotanticClient, *, position_ms: int, device_id: Optional[str] = None
) -> APICallModel[SeekToPositionRequest, RawAPIResponse, None]:
    """Seek to position in currently playing track.

    Seeks to the given position in the user’s currently playing track. This API only works for users
    who have Spotify Premium. The order of execution is not guaranteed when you use this API with
    other Player API endpoints.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        position_ms: The position in milliseconds to seek to.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = SeekToPositionRequest.build(position_ms=position_ms, device_id=device_id)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
