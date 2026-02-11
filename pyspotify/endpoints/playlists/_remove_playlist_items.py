from typing import Optional
from typing import Sequence
from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import RemovePlaylistItemsRequest
from pyspotify.models.playlists.responses import PlaylistSnapshotResponseModel
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyEpisodeURI
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyTrackURI


async def remove_playlist_items(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
    snapshot_id: Optional[str] = None,
) -> APICallModel[RemovePlaylistItemsRequest, APIResponse, PlaylistSnapshotResponseModel]:
    """Remove items from a playlist.

    Remove one or more items from a user's playlist.

    Args:
        client: PySpotifyClient instance.
        playlist_id: The Spotify ID of the playlist.
        uris: A list of Spotify URIs for the items to remove.
        snapshot_id: The playlist's snapshot ID.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = RemovePlaylistItemsRequest.build(
        playlist_id=playlist_id,
        uris=uris,
        snapshot_id=snapshot_id,
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistSnapshotResponseModel(**response)

    return APICallModel(request=request, response=response, data=data)
