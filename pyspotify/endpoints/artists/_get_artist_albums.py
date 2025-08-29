from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import AlbumTypes
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.artists.requests import GetArtistAlbumsRequest
from pyspotify.models.artists.requests import GetArtistAlbumsRequestParams
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedAlbumModel


async def get_artist_albums(
    client: PySpotifyClient,
    *,
    artist_id: SpotifyItemID,
    limit: int = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
    include_groups: Optional[Sequence[AlbumTypes]] = None,
) -> APICallModel[GetArtistAlbumsRequest, APIResponse, PagedResultModel[SimplifiedAlbumModel]]:
    request = GetArtistAlbumsRequest(
        endpoint=f"artists/{artist_id}/albums",
        params=GetArtistAlbumsRequestParams(
            artist_id=artist_id,
            limit=limit,
            offset=offset,
            market=market,
            include_groups=include_groups,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedAlbumModel](**response)

    return APICallModel(request=request, response=response, data=data)
