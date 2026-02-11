from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from pyspotify.models import RequestModel
from pyspotify.types import AuthScope


class GetCurrentUserPlaylistsRequestParams(BaseModel):
    """Params model for Get Current User's Playlists request."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of playlists to return."""

    offset: Annotated[int, Field(ge=0, le=100_000)]
    """The index of the first playlist to return."""


class GetCurrentUserPlaylistsRequest(RequestModel[GetCurrentUserPlaylistsRequestParams, None]):
    """Request model for Get Current User's Playlists endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.PLAYLIST_READ_PRIVATE}
    """Required authorization scopes for the request."""

    endpoint: Optional[str] = "me/playlists"
    """Endpoint associated with the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        offset: int = 0,
    ) -> GetCurrentUserPlaylistsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            limit: The maximum number of playlists to return.
            offset: The index of the first playlist to return.

        Returns:
            Validated Request object.
        """
        params = GetCurrentUserPlaylistsRequestParams(limit=limit, offset=offset)

        return cls(params=params)
