from __future__ import annotations

from http import HTTPMethod
from typing import Annotated

from pydantic import BaseModel
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class GetUserPlaylistsRequestParams(BaseModel):
    """Params model for Get User's Playlists request."""

    user_id: str
    """The Spotify user ID of the playlist owner."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of playlists to return."""

    offset: Annotated[int, Field(ge=0, le=100_000)]
    """The index of the first playlist to return."""


class GetUserPlaylistsRequest(RequestModel[GetUserPlaylistsRequestParams, None]):
    """Request model for Get User's Playlists endpoint."""

    required_scopes: set[Scope] = {Scope.PLAYLIST_READ_PRIVATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        user_id: str,
        limit: int = 20,
        offset: int = 0,
    ) -> GetUserPlaylistsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            user_id: The Spotify user ID of the playlist owner.
            limit: The maximum number of playlists to return.
            offset: The index of the first playlist to return.

        Returns:
            Validated Request object.
        """
        params = GetUserPlaylistsRequestParams(
            user_id=user_id,
            limit=limit,
            offset=offset,
        )
        endpoint = f"users/{user_id}/playlists"

        return cls(endpoint=endpoint, params=params)
