from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from spotantic.models import RequestBodyJsonModel
from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


class ChangePlaylistDetailsRequestParams(BaseModel):
    """Params model for Change Playlist Details request."""

    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the playlist."""


class ChangePlaylistDetailsRequestBody(RequestBodyJsonModel):
    """Body model for Change Playlist Details request."""

    name: Optional[str] = None
    """The new name for the playlist."""

    public: Optional[bool] = None
    """Whether the playlist should be public."""

    collaborative: Optional[bool] = None
    """Whether the playlist should be collaborative."""

    description: Optional[str] = None
    """The new description for the playlist."""


class ChangePlaylistDetailsRequest(RequestModel[ChangePlaylistDetailsRequestParams, ChangePlaylistDetailsRequestBody]):
    """Request model for Change Playlist Details endpoint."""

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
        name: Optional[str] = None,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> ChangePlaylistDetailsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist.
            name: The new name for the playlist.
            public: Whether the playlist should be public.
            collaborative: Whether the playlist should be collaborative.
            description: The new description for the playlist.

        Returns:
            Validated Request object.
        """
        params = ChangePlaylistDetailsRequestParams(playlist_id=playlist_id)
        body = ChangePlaylistDetailsRequestBody(
            name=name,
            public=public,
            collaborative=collaborative,
            description=description,
        )
        endpoint = f"playlists/{playlist_id}"

        return cls(endpoint=endpoint, params=params, body=body)
