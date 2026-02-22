from collections.abc import Sequence
from typing import Optional
from typing import Union

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import UpdatePlaylistItemsRequest
from spotantic.models.playlists.responses import PlaylistSnapshotResponseModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyEpisodeURI
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyTrackURI


async def update_playlist_items(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
    uris: Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]] = None,
    range_start: int,
    insert_before: int,
    range_length: int = 1,
    snapshot_id: Optional[str] = None,
) -> APICallModel[UpdatePlaylistItemsRequest, JsonAPIResponse, PlaylistSnapshotResponseModel]:
    """Reorder items in a playlist.

    Either reorder or replace items in a playlist depending on the request's parameters.
    To reorder items, include range_start, insert_before, range_length and snapshot_id in the request's body.
    To replace items, include uris as either a query parameter or in the request's body. Replacing items in
    a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in
    a playlist. These operations can't be applied together in a single request.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        playlist_id: The Spotify ID of the playlist.
        uris: A list of Spotify URIs for the items to update.
        range_start: The position of the first item to be reordered.
        insert_before: The position where the items should be inserted.
        range_length: The number of items to be reordered. Default is 1.
        snapshot_id: The playlist's snapshot ID.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = UpdatePlaylistItemsRequest.build(
        playlist_id=playlist_id,
        uris=uris,
        range_start=range_start,
        insert_before=insert_before,
        range_length=range_length,
        snapshot_id=snapshot_id,
    )
    response = await client.request_json(request)
    data = PlaylistSnapshotResponseModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
