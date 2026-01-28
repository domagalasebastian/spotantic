from __future__ import annotations

from http import HTTPMethod
from typing import Optional
from typing import Set

from pydantic import BaseModel

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestHeadersModel
from pyspotify.models import RequestModel


class FollowPlaylistRequestParams(BaseModel):
    """Params model for Follow Playlist request."""

    playlist_id: SpotifyItemID
    """The Spotify ID for the playlist."""


class FollowPlaylistRequestBody(BaseModel):
    """Body model for Follow Playlist request."""

    public: Optional[bool] = None
    """If true the playlist will be followed publicly.
    If false it will be followed privately.
    """


class FollowPlaylistRequest(RequestModel[FollowPlaylistRequestParams, FollowPlaylistRequestBody]):
    """Request model for Follow Playlist endpoint."""

    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
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
        public: bool = True,
    ) -> FollowPlaylistRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID for the playlist.
            public: If true the playlist will be followed publicly.
                If false it will be followed privately.

        Returns:
            Validated Request object.
        """
        params = FollowPlaylistRequestParams(
            playlist_id=playlist_id,
        )
        body = FollowPlaylistRequestBody(
            public=public,
        )
        endpoint = f"playlists/{playlist_id}/followers"

        return cls(endpoint=endpoint, params=params, body=body)
