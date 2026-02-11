from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import TransferPlaybackRequest
from pyspotify.types import APIResponse


async def transfer_playback(
    client: PySpotifyClient, *, device_ids: Sequence[str], play: Optional[bool] = None
) -> APICallModel[TransferPlaybackRequest, APIResponse, None]:
    """Transfer playback to a new device.

    Transfer playback to a new device and optionally begin playback. This API only works for users
    who have Spotify Premium. The order of execution is not guaranteed when you use this API with
    other Player API endpoints.

    Args:
        client: PySpotifyClient instance.
        device_ids: A list of the device IDs on which playback should be started/transferred to.
        play: True to enable playback on the new device. If false or not provided,
         the user's current playback will continue on the previous device.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = TransferPlaybackRequest.build(device_ids=device_ids, play=play)
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
