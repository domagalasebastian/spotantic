from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from spotantic.models import RequestModel
from spotantic.types import SpotifyLocaleID


class GetSeveralBrowseCategoriesRequestParams(BaseModel):
    """Params model for Get Several Browse Categories request."""

    locale: Optional[SpotifyLocaleID] = None
    """
    The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code,
    joined by an underscore.
    """

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""


class GetSeveralBrowseCategoriesRequest(RequestModel[GetSeveralBrowseCategoriesRequestParams, None]):
    """Request model for Get Several Browse Categories endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "browse/categories"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        offset: int = 0,
        locale: Optional[SpotifyLocaleID] = None,
    ) -> GetSeveralBrowseCategoriesRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first item to return. Default: 0 (the first item).
             Use with limit to get the next set of items.
            locale: The desired language, consisting of an ISO 639-1 language code and an ISO 3166-1 alpha-2 country code,
             joined by an underscore.

        Returns:
            Validated Request object.
        """
        params = GetSeveralBrowseCategoriesRequestParams(
            locale=locale,
            limit=limit,
            offset=offset,
        )

        return cls(params=params)
