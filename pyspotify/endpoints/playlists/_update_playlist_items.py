from typing import Optional
from typing import Sequence
from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import UpdatePlaylistItemsRequest
from pyspotify.models.playlists.responses import PlaylistSnapshotResponseModel


async def update_playlist_items(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    uris: Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]] = None,
    range_start: int,
    insert_before: int,
    range_length: int = 1,
    snapshot_id: Optional[str] = None,
) -> APICallModel[UpdatePlaylistItemsRequest, APIResponse, PlaylistSnapshotResponseModel]:
    request = UpdatePlaylistItemsRequest.build(
        playlist_id=playlist_id,
        uris=uris,
        range_start=range_start,
        insert_before=insert_before,
        range_length=range_length,
        snapshot_id=snapshot_id,
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistSnapshotResponseModel(**response)

    return APICallModel(request=request, response=response, data=data)
