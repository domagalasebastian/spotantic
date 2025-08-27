from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetCurrentlyPlayingTrackRequest
from pyspotify.models.player.requests import GetCurrentlyPlayingTrackRequestParams
from pyspotify.models.spotify import CurrentlyPlayingItemModel


async def get_currently_playing_track(
    client: PySpotifyClient,
    *,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetCurrentlyPlayingTrackRequest, APIResponse, CurrentlyPlayingItemModel]:
    request = GetCurrentlyPlayingTrackRequest(
        endpoint="me/player/currently-playing",
        params=GetCurrentlyPlayingTrackRequestParams(
            additional_types=additional_types,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = CurrentlyPlayingItemModel(**response)

    return APICallModel(request=request, response=response, data=data)
