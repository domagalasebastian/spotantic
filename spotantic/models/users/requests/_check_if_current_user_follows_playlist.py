from __future__ import annotations

from http import HTTPMethod

from pydantic import BaseModel

from spotantic.models import RequestModel
from spotantic.types import SpotifyItemID


class CheckIfCurrentUserFollowsPlaylistRequestParams(BaseModel):
    """Params model for Check If Current User Follows Playlist request."""

    playlist_id: SpotifyItemID
    """The Spotify ID for the playlist."""


class CheckIfCurrentUserFollowsPlaylistRequest(RequestModel[CheckIfCurrentUserFollowsPlaylistRequestParams, None]):
    """Request model for Check If Current User Follows Playlist endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
    ) -> CheckIfCurrentUserFollowsPlaylistRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID for the playlist.

        Returns:
            Validated Request object.
        """
        params = CheckIfCurrentUserFollowsPlaylistRequestParams(
            playlist_id=playlist_id,
        )
        endpoint = f"playlists/{playlist_id}/followers/contains"

        return cls(endpoint=endpoint, params=params)
