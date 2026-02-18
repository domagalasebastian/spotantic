from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


class GetShowRequestParams(BaseModel):
    """Params model for Get Show request."""

    model_config = ConfigDict(serialize_by_alias=True)

    show_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the show."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetShowRequest(RequestModel[GetShowRequestParams, None]):
    """Request model for Get Show endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_PLAYBACK_POSITION}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        show_id: SpotifyItemID,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetShowRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            show_id: The Spotify ID for the show.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        endpoint = f"shows/{show_id}"

        params = GetShowRequestParams(
            show_id=show_id,
            market=market,
        )

        return cls(endpoint=endpoint, params=params)
