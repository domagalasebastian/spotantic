from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetAlbumTracksRequestParams(BaseModel):
    """Params model for Get Album Tracks request."""

    model_config = ConfigDict(serialize_by_alias=True)

    album_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the album."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetAlbumTracksRequest(RequestModel[GetAlbumTracksRequestParams, None]):
    """Request model for Get Album Tracks endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        album_id: SpotifyItemID,
        limit: int = 20,
        offset: int = 0,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetAlbumTracksRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            album_id: The Spotify ID for the album.
            limit: The maximum number of items to return.
            offset: The index of the first item to return.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetAlbumTracksRequestParams(
            album_id=album_id,
            limit=limit,
            offset=offset,
            market=market,
        )

        endpoint = f"albums/{album_id}/tracks"

        return cls(endpoint=endpoint, params=params)
