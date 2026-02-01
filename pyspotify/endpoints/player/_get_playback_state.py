from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetPlaybackStateRequest
from pyspotify.models.spotify import PlaybackStateModel


async def get_playback_state(
    client: PySpotifyClient,
    *,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaybackStateRequest, APIResponse, PlaybackStateModel]:
    """Get the user's playback state.

    Get information about the user’s current playback state, including track or episode, progress, and active device.

    Args:
        client: PySpotifyClient instance.
        additional_types: A list of item types that your client supports besides the default track type.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetPlaybackStateRequest.build(
        additional_types=additional_types,
        market=market,
    )
    response = await client.request(request)
    assert response is not None
    data = PlaybackStateModel(**response)

    return APICallModel(request=request, response=response, data=data)
