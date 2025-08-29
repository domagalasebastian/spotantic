from typing import List
from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.artists.requests import GetArtistTopTracksRequest
from pyspotify.models.artists.requests import GetArtistTopTracksRequestParams
from pyspotify.models.spotify import TrackModel


async def get_artist_top_tracks(
    client: PySpotifyClient, *, artist_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetArtistTopTracksRequest, APIResponse, List[TrackModel]]:
    request = GetArtistTopTracksRequest(
        endpoint=f"artists/{artist_id}/top-tracks",
        params=GetArtistTopTracksRequestParams(
            artist_id=artist_id,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = [TrackModel(**track_data) for track_data in response["tracks"]]

    return APICallModel(request=request, response=response, data=data)
