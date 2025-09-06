from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import GetPlaylistRequest
from pyspotify.models.playlists.requests import GetPlaylistRequestParams
from pyspotify.models.spotify import PlaylistModel


async def get_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    fields: Optional[str] = None,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaylistRequest, APIResponse, PlaylistModel]:
    request = GetPlaylistRequest(
        endpoint=f"playlists/{playlist_id}",
        params=GetPlaylistRequestParams(
            playlist_id=playlist_id,
            fields=fields,
            additional_types=additional_types,
            market=market,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistModel(**response)

    return APICallModel(request=request, response=response, data=data)
