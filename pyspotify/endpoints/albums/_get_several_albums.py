from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetSeveralAlbumsRequest
from pyspotify.models.spotify import AlbumModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


async def get_several_albums(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralAlbumsRequest, APIResponse, list[AlbumModel]]:
    """Get Spotify catalog information for multiple albums identified by their Spotify IDs.

    Args:
        client: PySpotifyClient instance.
        album_ids: A list of Spotify artist IDs to retrieve.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetSeveralAlbumsRequest.build(album_ids=album_ids, market=market)
    response = await client.request(request)
    assert response is not None
    data = [AlbumModel(**album_data) for album_data in response["albums"]]

    return APICallModel(request=request, response=response, data=data)
