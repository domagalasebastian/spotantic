from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Set

from pydantic import BaseModel
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class GetUserPlaylistsRequestParams(BaseModel):
    user_id: str
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: Annotated[int, Field(ge=0, le=100_000)]


class GetUserPlaylistsRequest(RequestModel[GetUserPlaylistsRequestParams, None]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_READ_PRIVATE}
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(
        cls,
        *,
        user_id: str,
        limit: int = 20,
        offset: int = 0,
    ) -> GetUserPlaylistsRequest:
        params = GetUserPlaylistsRequestParams(
            user_id=user_id,
            limit=limit,
            offset=offset,
        )
        endpoint = f"users/{user_id}/playlists"

        return cls(endpoint=endpoint, params=params)
