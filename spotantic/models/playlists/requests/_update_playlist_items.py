from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyEpisodeURI
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyTrackURI


class UpdatePlaylistItemsRequestParams(BaseModel):
    """Params model for Update Playlist Items request."""

    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the playlist."""

    uris: Annotated[
        Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]],
        Field(None, max_length=100),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify URIs for the items to update."""


class UpdatePlaylistItemsRequestBody(BaseModel):
    """Body model for Update Playlist Items request."""

    uris: Annotated[Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]], Field(None, max_length=100)]
    """A list of Spotify URIs for the items to update."""

    range_start: int
    """The position of the first item to be moved."""

    insert_before: int
    """The position where the items should be inserted."""

    range_length: Optional[int] = None
    """The number of items to be moved."""

    snapshot_id: Optional[str] = None
    """The playlist's snapshot ID."""


class UpdatePlaylistItemsRequest(RequestModel[UpdatePlaylistItemsRequestParams, UpdatePlaylistItemsRequestBody]):
    """Request model for Update Playlist Items endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.PLAYLIST_MODIFY_PRIVATE, AuthScope.PLAYLIST_MODIFY_PUBLIC}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        uris: Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]] = None,
        range_start: int,
        insert_before: int,
        range_length: int = 1,
        snapshot_id: Optional[str] = None,
    ) -> UpdatePlaylistItemsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist.
            uris: A list of Spotify URIs for the items to update.
            range_start: The position of the first item to be moved.
            insert_before: The position where the items should be inserted.
            range_length: The number of items to be moved.
            snapshot_id: The playlist's snapshot ID.

        Returns:
            Validated Request object.
        """
        params = UpdatePlaylistItemsRequestParams(
            playlist_id=playlist_id,
            uris=uris,
        )
        body = UpdatePlaylistItemsRequestBody(
            uris=uris,
            range_start=range_start,
            insert_before=insert_before,
            range_length=range_length,
            snapshot_id=snapshot_id,
        )
        endpoint = f"playlists/{playlist_id}/tracks"

        return cls(endpoint=endpoint, params=params, body=body)
