from typing import Optional
from typing import Sequence
from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import RemovePlaylistItemsRequest
from pyspotify.models.playlists.responses import PlaylistSnapshotResponseModel


async def remove_playlist_items(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
    snapshot_id: Optional[str] = None,
) -> APICallModel[RemovePlaylistItemsRequest, APIResponse, PlaylistSnapshotResponseModel]:
    request = RemovePlaylistItemsRequest.build(
        playlist_id=playlist_id,
        uris=uris,
        snapshot_id=snapshot_id,
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistSnapshotResponseModel(**response)

    return APICallModel(request=request, response=response, data=data)
