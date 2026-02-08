from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetUserSavedAlbumsRequestParams(BaseModel):
    """Params model for Get User Saved Albums request."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetUserSavedAlbumsRequest(RequestModel[GetUserSavedAlbumsRequestParams, None]):
    """Request model for Get User Saved Albums endpoint."""

    required_scopes: set[Scope] = {Scope.USER_LIBRARY_READ}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/albums"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        offset: int = 0,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetUserSavedAlbumsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            limit: The maximum number of items to return.
            offset: The index of the first item to return.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetUserSavedAlbumsRequestParams(
            limit=limit,
            offset=offset,
            market=market,
        )

        return cls(params=params)
