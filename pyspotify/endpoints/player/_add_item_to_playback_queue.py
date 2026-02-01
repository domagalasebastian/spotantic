from typing import Optional
from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import AddItemToPlaybackQueueRequest


async def add_item_to_playback_queue(
    client: PySpotifyClient, *, uri: Union[SpotifyEpisodeURI, SpotifyTrackURI], device_id: Optional[str] = None
) -> APICallModel[AddItemToPlaybackQueueRequest, APIResponse, None]:
    """Add an item to the end of the user's playback queue.

    Add an item to be played next in the user's current playback queue. This API only works for users
    who have Spotify Premium. The order of execution is not guaranteed when you use this API with
    other Player API endpoints.

    Args:
        client: PySpotifyClient instance.
        uri: The Spotify URI of the item to add to the queue. Must be a track or episode URI.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = AddItemToPlaybackQueueRequest.build(uri=uri, device_id=device_id)
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
