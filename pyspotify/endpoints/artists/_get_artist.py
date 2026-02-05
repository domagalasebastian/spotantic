from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.artists.requests import GetArtistRequest
from pyspotify.models.spotify import ArtistModel


async def get_artist(
    client: PySpotifyClient, *, artist_id: SpotifyItemID
) -> APICallModel[GetArtistRequest, APIResponse, ArtistModel]:
    """Get Spotify catalog information for a single artist identified by their unique Spotify ID.

    Args:
        client: PySpotifyClient instance.
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
