from typing import Sequence

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.artists.requests import GetSeveralArtistsRequest
from spotantic.models.spotify import ArtistModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def get_several_artists(
    client: SpotanticClient, *, artist_ids: Sequence[SpotifyItemID]
) -> APICallModel[GetSeveralArtistsRequest, APIResponse, list[ArtistModel]]:
    """Get Spotify catalog information for several artists based on their Spotify IDs.

    Args:
        client: SpotanticClient instance.
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
