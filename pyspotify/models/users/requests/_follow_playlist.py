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
    playlist_id: SpotifyItemID


class FollowPlaylistRequestBody(BaseModel):
    public: Optional[bool] = None


class FollowPlaylistRequest(RequestModel[FollowPlaylistRequestParams, FollowPlaylistRequestBody]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
    method_type: HTTPMethod = HTTPMethod.PUT
    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        public: bool = True,
    ) -> FollowPlaylistRequest:
        params = FollowPlaylistRequestParams(
            playlist_id=playlist_id,
        )
        body = FollowPlaylistRequestBody(
            public=public,
        )
        endpoint = f"playlists/{playlist_id}/followers"

        return cls(endpoint=endpoint, params=params, body=body)
