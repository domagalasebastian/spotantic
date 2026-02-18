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


class AddItemsToPlaylistRequestParams(BaseModel):
    """Params model for Add Items to Playlist request."""

    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the playlist."""

    position: Optional[int] = None
    """The position to insert the items."""

    uris: Annotated[
        Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]],
        Field(max_length=100),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ] = None
    """A list of Spotify URIs for the items to add."""


class AddItemsToPlaylistRequestBody(BaseModel):
    """Body model for Add Items to Playlist request."""

    uris: Annotated[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]], Field(max_length=100)]
    """A list of Spotify URIs for the items to add."""

    position: Optional[int] = None
    """The position to insert the items."""


class AddItemsToPlaylistRequest(RequestModel[AddItemsToPlaylistRequestParams, AddItemsToPlaylistRequestBody]):
    """Request model for Add Items to Playlist endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.PLAYLIST_MODIFY_PRIVATE, AuthScope.PLAYLIST_MODIFY_PUBLIC}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.POST
    """HTTP method for the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
        position: Optional[int] = None,
    ) -> AddItemsToPlaylistRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist.
            uris: A list of Spotify URIs for the items to add.
            position: The position to insert the items, or None to add to the end.

        Returns:
            Validated Request object.
        """
        params = AddItemsToPlaylistRequestParams(playlist_id=playlist_id)
        body = AddItemsToPlaylistRequestBody(uris=uris, position=position)
        endpoint = f"playlists/{playlist_id}/tracks"

        return cls(endpoint=endpoint, params=params, body=body)
