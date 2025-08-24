from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.albums.requests import GetAlbumTracksRequest
from pyspotify.models.albums.requests import GetAlbumTracksRequestParams
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedTrackModel


async def get_album_tracks(
    client: PySpotifyClient,
    *,
    album_id: SpotifyItemID,
    limit: int = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetAlbumTracksRequest, APIResponse, PagedResultModel[SimplifiedTrackModel]]:
    request = GetAlbumTracksRequest(
        endpoint=f"albums/{album_id}/tracks",
        params=GetAlbumTracksRequestParams(
            album_id=album_id,
            limit=limit,
            offset=offset,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedTrackModel](**response)

    return APICallModel(request=request, response=response, data=data)
