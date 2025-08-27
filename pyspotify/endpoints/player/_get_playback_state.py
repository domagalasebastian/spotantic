from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetPlaybackStateRequest
from pyspotify.models.player.requests import GetPlaybackStateRequestParams
from pyspotify.models.spotify import PlaybackStateModel


async def get_playback_state(
    client: PySpotifyClient,
    *,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaybackStateRequest, APIResponse, PlaybackStateModel]:
    request = GetPlaybackStateRequest(
        endpoint="me/player",
        params=GetPlaybackStateRequestParams(
            additional_types=additional_types,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PlaybackStateModel(**response)

    return APICallModel(request=request, response=response, data=data)
