from collections.abc import Sequence
from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import GetPlaybackStateRequest
from spotantic.models.spotify import PlaybackStateModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


async def get_playback_state(
    client: SpotanticClient,
    *,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaybackStateRequest, JsonAPIResponse, PlaybackStateModel]:
    """Get information about the user’s current playback state, including track or episode, progress,
    and active device.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
    response = await client.request_json(request)
    data = PlaybackStateModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
