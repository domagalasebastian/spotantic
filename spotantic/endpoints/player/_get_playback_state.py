from typing import Optional
from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import GetPlaybackStateRequest
from spotantic.models.spotify import PlaybackStateModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


async def get_playback_state(
    client: SpotanticClient,
    *,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaybackStateRequest, APIResponse, PlaybackStateModel]:
    """Get the user's playback state.

    Get information about the user’s current playback state, including track or episode, progress, and active device.

    Args:
        client: SpotanticClient instance.
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
