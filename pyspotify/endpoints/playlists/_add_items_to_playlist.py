from typing import Optional
from typing import Sequence
from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import AddItemsToPlaylistRequest
from pyspotify.models.playlists.responses import PlaylistSnapshotResponseModel


async def add_items_to_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
    position: Optional[int] = None,
) -> APICallModel[AddItemsToPlaylistRequest, APIResponse, PlaylistSnapshotResponseModel]:
    """Add items to a playlist.

    Add one or more items to a user's playlist.

    Args:
        client: PySpotifyClient instance.
        playlist_id: The Spotify ID of the playlist.
        uris: A list of Spotify URIs for the items to add.
        position: The position to insert the items, or None to add to the end.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = AddItemsToPlaylistRequest.build(
        playlist_id=playlist_id,
        uris=uris,
        position=position,
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistSnapshotResponseModel(**response)

    return APICallModel(request=request, response=response, data=data)
