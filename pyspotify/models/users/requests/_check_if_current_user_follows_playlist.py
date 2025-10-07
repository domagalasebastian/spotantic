from __future__ import annotations

from http import HTTPMethod

from pydantic import BaseModel

from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class CheckIfCurrentUserFollowsPlaylistRequestParams(BaseModel):
    playlist_id: SpotifyItemID


class CheckIfCurrentUserFollowsPlaylistRequest(RequestModel[CheckIfCurrentUserFollowsPlaylistRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
    ) -> CheckIfCurrentUserFollowsPlaylistRequest:
        params = CheckIfCurrentUserFollowsPlaylistRequestParams(
            playlist_id=playlist_id,
        )
        endpoint = f"playlists/{playlist_id}/followers/contains"

        return cls(endpoint=endpoint, params=params)
