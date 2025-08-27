from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import TransferPlaybackRequest
from pyspotify.models.player.requests import TransferPlaybackRequestBody


async def transfer_playback(
    client: PySpotifyClient, *, device_ids: Sequence[str], play: Optional[bool] = None
) -> APICallModel[TransferPlaybackRequest, APIResponse, None]:
    request = TransferPlaybackRequest(
        endpoint="me/player",
        body=TransferPlaybackRequestBody(
            device_ids=device_ids,
            play=play,
        ),
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
