from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.spotify import TrackModel
from pyspotify.models.tracks.requests import GetTrackRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_track(
    client: PySpotifyClient, *, track_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetTrackRequest, APIResponse, TrackModel]:
    """Get Spotify catalog information for a single track based on its Spotify ID.

    Get Spotify catalog information for a single track identified by its unique Spotify ID.

    Args:
        client: PySpotifyClient instance.
        track_id: The Spotify ID for the track.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetTrackRequest.build(track_id=track_id, market=market)
    response = await client.request(request)
    assert response is not None
    data = TrackModel(**response)

    return APICallModel(request=request, response=response, data=data)
