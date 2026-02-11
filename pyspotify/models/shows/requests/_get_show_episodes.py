from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.models import RequestModel
from pyspotify.types import AuthScope
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


class GetShowEpisodesRequestParams(BaseModel):
    """Params model for Get Show Episodes request."""

    model_config = ConfigDict(serialize_by_alias=True)

    show_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the show."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetShowEpisodesRequest(RequestModel[GetShowEpisodesRequestParams, None]):
    """Request model for Get Show Episodes endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_PLAYBACK_POSITION}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        show_id: SpotifyItemID,
        limit: int = 20,
        offset: int = 0,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetShowEpisodesRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            show_id: The Spotify ID for the show.
            limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first item to return. Default: 0 (the first item).
              Use with limit to get the next set of items.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        endpoint = f"shows/{show_id}/episodes"

        params = GetShowEpisodesRequestParams(
            show_id=show_id,
            limit=limit,
            offset=offset,
            market=market,
        )

        return cls(endpoint=endpoint, params=params)
