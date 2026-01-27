from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.spotify import TrackModel
from pyspotify.models.tracks.requests import GetSeveralTracksRequest


async def get_several_tracks(
    client: PySpotifyClient, *, track_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralTracksRequest, APIResponse, list[TrackModel]]:
    """Get Spotify catalog information for several tracks based on their Spotify IDs.

    Get Spotify catalog information for multiple tracks based on their Spotify IDs.

    Args:
        client: PySpotifyClient instance.
        track_ids: A list of the Spotify IDs for the tracks.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralTracksRequest.build(track_ids=track_ids, market=market)
    response = await client.request(request)
    assert response is not None
    data = [TrackModel(**track_data) for track_data in response["tracks"]]

    return APICallModel(request=request, response=response, data=data)
