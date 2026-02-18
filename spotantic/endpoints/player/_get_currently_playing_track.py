from typing import Optional
from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import GetCurrentlyPlayingTrackRequest
from spotantic.models.spotify import CurrentlyPlayingItemModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


async def get_currently_playing_track(
    client: SpotanticClient,
    *,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetCurrentlyPlayingTrackRequest, APIResponse, CurrentlyPlayingItemModel]:
    """Get the user's currently playing track.

    Get the object currently being played on the user's Spotify account.

    Args:
        client: SpotanticClient instance.
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
