from collections.abc import Sequence
from typing import Optional
from typing import Union

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import AddItemsToPlaylistRequest
from spotantic.models.playlists.responses import PlaylistSnapshotResponseModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyEpisodeURI
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyTrackURI


async def add_items_to_playlist(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
    uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
    position: Optional[int] = None,
) -> APICallModel[AddItemsToPlaylistRequest, JsonAPIResponse, PlaylistSnapshotResponseModel]:
    """Add one or more items to a user's playlist.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
    response = await client.request_json(request)
    data = PlaylistSnapshotResponseModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
