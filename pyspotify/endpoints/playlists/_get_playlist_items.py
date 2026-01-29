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
    """Get items of a playlist.

    Get full details of the items of a playlist owned by a Spotify user.

    Args:
        client: PySpotifyClient instance.
        playlist_id: The Spotify ID of the playlist.
        fields: Filters for the query: a comma-separated list of the fields to return.
        limit: The maximum number of items to return. Default is 20. Minimum is 1, maximum is 50.
        offset: The index of the first item to return. Default is 0.
        additional_types: A list of item types to include in the response.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
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
