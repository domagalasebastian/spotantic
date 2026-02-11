from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetCurrentlyPlayingTrackRequest
from pyspotify.models.spotify import CurrentlyPlayingItemModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemType
from pyspotify.types import SpotifyMarketID


async def get_currently_playing_track(
    client: PySpotifyClient,
    *,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetCurrentlyPlayingTrackRequest, APIResponse, CurrentlyPlayingItemModel]:
    """Get the user's currently playing track.

    Get the object currently being played on the user's Spotify account.

    Args:
        client: PySpotifyClient instance.
        additional_types: A list of item types that your client supports besides the default track type.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetCurrentlyPlayingTrackRequest.build(
        additional_types=additional_types,
        market=market,
    )
    response = await client.request(request)
    assert response is not None
    data = CurrentlyPlayingItemModel(**response)

    return APICallModel(request=request, response=response, data=data)
