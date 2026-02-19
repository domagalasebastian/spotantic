from collections.abc import Sequence
from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import GetPlaylistRequest
from spotantic.models.spotify import PlaylistModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


async def get_playlist(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
    fields: Optional[str] = None,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaylistRequest, APIResponse, PlaylistModel]:
    """Get a playlist owned by a Spotify user.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        playlist_id: The Spotify ID of the playlist.
        fields: Filters for the query: a comma-separated list of the fields to return.
        additional_types: A list of item types to include in the response.
        market: An ISO 3166-1 alpha-2 country code.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetPlaylistRequest.build(
        playlist_id=playlist_id,
        fields=fields,
        additional_types=additional_types,
        market=market,
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistModel(**response)

    return APICallModel(request=request, response=response, data=data)
