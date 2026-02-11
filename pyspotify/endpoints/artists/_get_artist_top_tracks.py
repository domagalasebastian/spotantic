from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.artists.requests import GetArtistTopTracksRequest
from pyspotify.models.spotify import TrackModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_artist_top_tracks(
    client: PySpotifyClient, *, artist_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetArtistTopTracksRequest, APIResponse, list[TrackModel]]:
    """Get Spotify catalog information about an artist's top tracks by country.

    Args:
        client: PySpotifyClient instance.
        artist_id: The Spotify ID for the artist.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetArtistTopTracksRequest.build(artist_id=artist_id, market=market)
    response = await client.request(request)
    assert response is not None
    data = [TrackModel(**track_data) for track_data in response["tracks"]]

    return APICallModel(request=request, response=response, data=data)
