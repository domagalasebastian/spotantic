from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.artists.requests import GetArtistRequest
from pyspotify.models.artists.requests import GetArtistRequestParams
from pyspotify.models.spotify import ArtistModel


async def get_artist(
    client: PySpotifyClient, *, artist_id: SpotifyItemID
) -> APICallModel[GetArtistRequest, APIResponse, ArtistModel]:
    request = GetArtistRequest(
        endpoint=f"artists/{artist_id}",
        params=GetArtistRequestParams(
            artist_id=artist_id,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = ArtistModel(**response)

    return APICallModel(request=request, response=response, data=data)
