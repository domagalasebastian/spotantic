from __future__ import annotations

from http import HTTPMethod

from pydantic import BaseModel

from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


class UnfollowPlaylistRequestParams(BaseModel):
    """Parameters for the Unfollow Playlist request model."""

    playlist_id: SpotifyItemID
    """The Spotify ID of the playlist to unfollow."""


class UnfollowPlaylistRequest(RequestModel[UnfollowPlaylistRequestParams, None]):
    """Request model for Unfollow Playlist endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.PLAYLIST_MODIFY_PRIVATE, AuthScope.PLAYLIST_MODIFY_PUBLIC}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.DELETE
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
    ) -> UnfollowPlaylistRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist to unfollow.

        Returns:
            Validated Request object.
        """
        params = UnfollowPlaylistRequestParams(
            playlist_id=playlist_id,
        )
        endpoint = f"playlists/{playlist_id}/followers"

        return cls(endpoint=endpoint, params=params)
