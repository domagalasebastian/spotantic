from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SetPlaybackVolumeRequest
from pyspotify.models.player.requests import SetPlaybackVolumeRequestParams


async def set_playback_volume(
    client: PySpotifyClient, *, volume_percent: int, device_id: Optional[str] = None
) -> APICallModel[SetPlaybackVolumeRequest, APIResponse, None]:
    request = SetPlaybackVolumeRequest(
        endpoint="me/player/volume",
        params=SetPlaybackVolumeRequestParams(
            volume_percent=volume_percent,
            device_id=device_id,
        ),
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
