from typing import Optional
from typing import Sequence

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import GetPlaylistRequest
from pyspotify.models.spotify import PlaylistModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyItemType
from pyspotify.types import SpotifyMarketID


async def get_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    fields: Optional[str] = None,
    additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> APICallModel[GetPlaylistRequest, APIResponse, PlaylistModel]:
    """Get a playlist.

    Get a playlist owned by a Spotify user.

    Args:
        client: PySpotifyClient instance.
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
