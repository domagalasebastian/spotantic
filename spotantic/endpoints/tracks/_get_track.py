from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import TrackModel
from spotantic.models.tracks.requests import GetTrackRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


async def get_track(
    client: SpotanticClient, *, track_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetTrackRequest, APIResponse, TrackModel]:
    """Get Spotify catalog information for a single track based on its Spotify ID.

    Get Spotify catalog information for a single track identified by its unique Spotify ID.

    Args:
        client: SpotanticClient instance.
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
