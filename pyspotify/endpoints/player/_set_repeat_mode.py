from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import RepeatMode
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SetRepeatModeRequest
from pyspotify.models.player.requests import SetRepeatModeRequestParams


async def set_repeat_mode(
    client: PySpotifyClient, *, state: RepeatMode, device_id: Optional[str] = None
) -> APICallModel[SetRepeatModeRequest, APIResponse, None]:
    request = SetRepeatModeRequest(
        endpoint="me/player/repeat",
        params=SetRepeatModeRequestParams(
            state=state,
            device_id=device_id,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
