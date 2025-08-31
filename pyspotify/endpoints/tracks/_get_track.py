from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.spotify import TrackModel
from pyspotify.models.tracks.requests import GetTrackRequest
from pyspotify.models.tracks.requests import GetTrackRequestParams


async def get_track(
    client: PySpotifyClient, *, track_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetTrackRequest, APIResponse, TrackModel]:
    request = GetTrackRequest(
        endpoint=f"tracks/{track_id}",
        params=GetTrackRequestParams(
            track_id=track_id,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = TrackModel(**response)

    return APICallModel(request=request, response=response, data=data)
