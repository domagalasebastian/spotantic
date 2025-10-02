from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Set

from pydantic import BaseModel
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class GetCurrentUserPlaylistsRequestParams(BaseModel):
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: Annotated[int, Field(ge=0, le=100_000)]


class GetCurrentUserPlaylistsRequest(RequestModel[GetCurrentUserPlaylistsRequestParams, None]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_READ_PRIVATE}
    endpoint: Optional[str] = "me/playlists"
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        offset: int = 0,
    ) -> GetCurrentUserPlaylistsRequest:
        params = GetCurrentUserPlaylistsRequestParams(limit=limit, offset=offset)

        return cls(params=params)
