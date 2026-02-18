from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyMarketID


class GetUserSavedEpisodesRequestParams(BaseModel):
    """Params model for Get User Saved Episodes request."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetUserSavedEpisodesRequest(RequestModel[GetUserSavedEpisodesRequestParams, None]):
    """Request model for Get User Saved Episodes endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_LIBRARY_READ, AuthScope.USER_READ_PLAYBACK_POSITION}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/episodes"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        offset: int = 0,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetUserSavedEpisodesRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first item to return. Default: 0 (the first item).
             Use with limit to get the next set of items.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetUserSavedEpisodesRequestParams(
            limit=limit,
            offset=offset,
            market=market,
        )

        return cls(params=params)
