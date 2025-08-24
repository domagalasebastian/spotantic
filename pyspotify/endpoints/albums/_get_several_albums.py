from typing import List
from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetSeveralAlbumsRequest
from pyspotify.models.albums.requests import GetSeveralAlbumsRequestParams
from pyspotify.models.spotify import AlbumModel


async def get_several_albums(
    client: PySpotifyClient, *, album_ids: Sequence[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> APICallModel[GetSeveralAlbumsRequest, APIResponse, List[AlbumModel]]:
    request = GetSeveralAlbumsRequest(
        endpoint="albums",
        params=GetSeveralAlbumsRequestParams(
            album_ids=album_ids,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = [AlbumModel(**album_data) for album_data in response["albums"]]

    return APICallModel(request=request, response=response, data=data)
