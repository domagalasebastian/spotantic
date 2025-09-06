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
from pyspotify.models.playlists.requests import RemovePlaylistItemsRequestBody
from pyspotify.models.playlists.requests import RemovePlaylistItemsRequestParams


async def remove_playlist_items(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
    snapshot_id: Optional[str] = None,
) -> APICallModel[RemovePlaylistItemsRequest, APIResponse, None]:
    request = RemovePlaylistItemsRequest(
        endpoint=f"playlists/{playlist_id}/tracks",
        params=RemovePlaylistItemsRequestParams(
            playlist_id=playlist_id,
        ),
        body=RemovePlaylistItemsRequestBody(
            tracks=uris,
            snapshot_id=snapshot_id,
        ),
    )
    response = await client.request(request)
    assert response is not None
    # TODO: Add response model

    return APICallModel(request=request, response=response, data=None)
