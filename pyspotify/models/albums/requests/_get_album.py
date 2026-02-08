from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetAlbumRequestParams(BaseModel):
    """Params model for Get Album request."""

    model_config = ConfigDict(serialize_by_alias=True)

    album_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the album."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetAlbumRequest(RequestModel[GetAlbumRequestParams, None]):
    """Request model for Get Album endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        album_id: SpotifyItemID,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetAlbumRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            album_id: The Spotify ID for the album.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetAlbumRequestParams(
            album_id=album_id,
            market=market,
        )

        endpoint = f"albums/{album_id}"

        return cls(endpoint=endpoint, params=params)
