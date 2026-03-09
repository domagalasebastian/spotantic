from __future__ import annotations

from http import HTTPMethod

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from spotantic.models import RequestModel
from spotantic.types import SpotifyItemID


class GetPlaylistCoverImageRequestParams(BaseModel):
    """Params model for Get Playlist Cover Image request."""

    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the playlist."""


class GetPlaylistCoverImageRequest(RequestModel[GetPlaylistCoverImageRequestParams, None]):
    """Request model for Get Playlist Cover Image endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
    ) -> GetPlaylistCoverImageRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist.

        Returns:
            Validated Request object.
        """
        params = GetPlaylistCoverImageRequestParams(playlist_id=playlist_id)
        endpoint = f"playlists/{playlist_id}/images"

        return cls(endpoint=endpoint, params=params)
