from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import SkipToNextRequest
from pyspotify.models.player.requests import SkipToNextRequestParams


async def skip_to_next(
    client: PySpotifyClient, *, device_id: Optional[str] = None
) -> APICallModel[SkipToNextRequest, APIResponse, None]:
    request = SkipToNextRequest(
        endpoint="me/player/next",
        params=SkipToNextRequestParams(
            device_id=device_id,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
