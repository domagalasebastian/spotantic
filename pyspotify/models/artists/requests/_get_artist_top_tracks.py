from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.models import RequestModel
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


class GetArtistTopTracksRequestParams(BaseModel):
    """Params model for Get Artist Top Tracks request."""

    model_config = ConfigDict(serialize_by_alias=True)

    artist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the artist."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetArtistTopTracksRequest(RequestModel[GetArtistTopTracksRequestParams, None]):
    """Request model for Get Artist Top Tracks endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        artist_id: SpotifyItemID,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetArtistTopTracksRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            artist_id: The Spotify ID for the artist.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetArtistTopTracksRequestParams(
            artist_id=artist_id,
            market=market,
        )

        endpoint = f"artists/{artist_id}/top-tracks"

        return cls(endpoint=endpoint, params=params)
