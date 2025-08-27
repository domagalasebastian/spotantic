from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SeekToPositionRequest
from pyspotify.models.player.requests import SeekToPositionRequestParams


async def seek_to_position(
    client: PySpotifyClient, *, position_ms: int, device_id: Optional[str] = None
) -> APICallModel[SeekToPositionRequest, APIResponse, None]:
    request = SeekToPositionRequest(
        endpoint="me/player/seek",
        params=SeekToPositionRequestParams(
            position_ms=position_ms,
            device_id=device_id,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
