from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import GetPlaylistItemsRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import PlaylistTrackModel


async def get_playlist_items(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    fields: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaylistItemsRequest, APIResponse, PagedResultModel[PlaylistTrackModel]]:
    request = GetPlaylistItemsRequest.build(
        playlist_id=playlist_id,
        fields=fields,
        limit=limit,
        offset=offset,
        additional_types=additional_types,
        market=market,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[PlaylistTrackModel](**response)

    return APICallModel(request=request, response=response, data=data)
