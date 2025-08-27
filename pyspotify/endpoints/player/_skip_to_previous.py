from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SkipToPreviousRequest
from pyspotify.models.player.requests import SkipToPreviousRequestParams


async def skip_to_previous(
    client: PySpotifyClient, *, device_id: Optional[str] = None
) -> APICallModel[SkipToPreviousRequest, APIResponse, None]:
    request = SkipToPreviousRequest(
        endpoint="me/player/previous",
        params=SkipToPreviousRequestParams(
            device_id=device_id,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
