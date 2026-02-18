from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic.functional_serializers import PlainSerializer

from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyEpisodeURI
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyTrackURI


class RemovePlaylistItemsRequestParams(BaseModel):
    """Params model for Remove Playlist Items request."""

    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the playlist."""


class RemovePlaylistItemsRequestBody(BaseModel):
    """Body model for Remove Playlist Items request."""

    tracks: Annotated[
        Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
        Field(max_length=100),
        PlainSerializer(lambda seq: [{"uri": uri} for uri in seq], return_type=list[dict[str, str]]),
    ]
    """A list of Spotify URIs for the items to remove."""

    snapshot_id: Optional[str] = None
    """The playlist's snapshot ID."""


class RemovePlaylistItemsRequest(RequestModel[RemovePlaylistItemsRequestParams, RemovePlaylistItemsRequestBody]):
    """Request model for Remove Playlist Items endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.PLAYLIST_MODIFY_PRIVATE, AuthScope.PLAYLIST_MODIFY_PUBLIC}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.DELETE
    """HTTP method for the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
        snapshot_id: Optional[str] = None,
    ) -> RemovePlaylistItemsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist.
            uris: A list of Spotify URIs for the items to remove.
            snapshot_id: The playlist's snapshot ID.

        Returns:
            Validated Request object.
        """
        params = RemovePlaylistItemsRequestParams(playlist_id=playlist_id)
        body = RemovePlaylistItemsRequestBody(
            tracks=uris,
            snapshot_id=snapshot_id,
        )
        endpoint = f"playlists/{playlist_id}/tracks"

        return cls(endpoint=endpoint, params=params, body=body)
