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
    request = AddItemsToPlaylistRequest.build(
        playlist_id=playlist_id,
        uris=uris,
        position=position,
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistSnapshotResponseModel(**response)

    return APICallModel(request=request, response=response, data=data)
