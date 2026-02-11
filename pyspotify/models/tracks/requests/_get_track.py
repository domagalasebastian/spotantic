from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.models import RequestModel
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


class GetTrackRequestParams(BaseModel):
    """Params model for Get Track request."""

    model_config = ConfigDict(serialize_by_alias=True)

    track_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the track."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetTrackRequest(RequestModel[GetTrackRequestParams, None]):
    """Request model for Get Track endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        track_id: SpotifyItemID,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetTrackRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            track_id: The Spotify ID for the track.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        endpoint = f"tracks/{track_id}"

        params = GetTrackRequestParams(
            track_id=track_id,
            market=market,
        )

        return cls(endpoint=endpoint, params=params)
