from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.artists.requests import GetSeveralArtistsRequest
from pyspotify.models.spotify import ArtistModel


async def get_several_artists(
    client: PySpotifyClient, *, artist_ids: Sequence[SpotifyItemID]
) -> APICallModel[GetSeveralArtistsRequest, APIResponse, list[ArtistModel]]:
    """Get Spotify catalog information for several artists based on their Spotify IDs.

    Args:
        client: PySpotifyClient instance.
        artist_ids: A list of Spotify artist IDs to retrieve.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralArtistsRequest.build(
        artist_ids=artist_ids,
    )
    response = await client.request(request)
    assert response is not None
    data = [ArtistModel(**artist_data) for artist_data in response["artists"]]

    return APICallModel(request=request, response=response, data=data)
