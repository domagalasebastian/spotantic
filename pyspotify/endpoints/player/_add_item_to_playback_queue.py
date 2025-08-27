from typing import Optional
from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import AddItemToPlaybackQueueRequest
from pyspotify.models.player.requests import AddItemToPlaybackQueueRequestParams


async def add_item_to_playback_queue(
    client: PySpotifyClient, *, uri: Union[SpotifyEpisodeURI, SpotifyTrackURI], device_id: Optional[str] = None
) -> APICallModel[AddItemToPlaybackQueueRequest, APIResponse, None]:
    request = AddItemToPlaybackQueueRequest(
        endpoint="me/player/queue",
        params=AddItemToPlaybackQueueRequestParams(
            uri=uri,
            device_id=device_id,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
