from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.artists.requests import GetArtistRequest
from spotantic.models.spotify import ArtistModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def get_artist(
    client: SpotanticClient, *, artist_id: SpotifyItemID
) -> APICallModel[GetArtistRequest, APIResponse, ArtistModel]:
    """Get Spotify catalog information for a single artist identified by their unique Spotify ID.

    Args:
        client: SpotanticClient instance.
        artist_id: The Spotify ID for the artist.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetArtistRequest.build(artist_id=artist_id)
    response = await client.request(request)
    assert response is not None
    data = ArtistModel(**response)

    return APICallModel(request=request, response=response, data=data)
