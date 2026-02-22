from collections.abc import Sequence
from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import GetPlaylistItemsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import PlaylistTrackModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


async def get_playlist_items(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
    fields: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaylistItemsRequest, JsonAPIResponse, PagedResultModel[PlaylistTrackModel]]:
    """Get full details of the items of a playlist owned by a Spotify user.

    Note: This endpoint is only accessible for playlists owned by the current user or
    playlists the user is a collaborator of. A 403 Forbidden status code will be returned if
    the user is neither the owner nor a collaborator of the playlist.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
    response = await client.request_json(request)
    data = PagedResultModel[PlaylistTrackModel].model_validate(response)

    return APICallModel(request=request, response=response, data=data)
