from __future__ import annotations

from http import HTTPMethod
from typing import Set

from pydantic import BaseModel

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class UnfollowPlaylistRequestParams(BaseModel):
    playlist_id: SpotifyItemID


class UnfollowPlaylistRequest(RequestModel[UnfollowPlaylistRequestParams, None]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
    method_type: HTTPMethod = HTTPMethod.DELETE

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
    ) -> UnfollowPlaylistRequest:
        params = UnfollowPlaylistRequestParams(
            playlist_id=playlist_id,
        )
        endpoint = f"playlists/{playlist_id}/followers"

        return cls(endpoint=endpoint, params=params)
