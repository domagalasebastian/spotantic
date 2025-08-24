from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetAlbumRequest
from pyspotify.models.albums.requests import GetAlbumRequestParams
from pyspotify.models.spotify import AlbumModel


async def get_album(
    client: PySpotifyClient, *, album_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetAlbumRequest, APIResponse, AlbumModel]:
    request = GetAlbumRequest(
        endpoint=f"albums/{album_id}",
        params=GetAlbumRequestParams(
            album_id=album_id,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = AlbumModel(**response)

    return APICallModel(request=request, response=response, data=data)
