from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetAlbumRequest
from pyspotify.models.spotify import AlbumModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_album(
    client: PySpotifyClient, *, album_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetAlbumRequest, APIResponse, AlbumModel]:
    """Get Spotify catalog information for a single album.

    Args:
        client: PySpotifyClient instance.
        album_id: The Spotify ID for the album.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAlbumRequest.build(album_id=album_id, market=market)
    response = await client.request(request)
    assert response is not None
    data = AlbumModel(**response)

    return APICallModel(request=request, response=response, data=data)
