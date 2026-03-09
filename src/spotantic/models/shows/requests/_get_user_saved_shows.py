from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from spotantic.models import RequestModel
from spotantic.types import AuthScope


class GetUserSavedShowsRequestParams(BaseModel):
    """Params model for Get User Saved Shows request."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""


class GetUserSavedShowsRequest(RequestModel[GetUserSavedShowsRequestParams, None]):
    """Request model for Get User Saved Shows endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_LIBRARY_READ}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/shows"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        offset: int = 0,
    ) -> GetUserSavedShowsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            limit: The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50.
            offset: The index of the first item to return. Default: 0 (the first item).

        Returns:
            Validated Request object.
        """
        params = GetUserSavedShowsRequestParams(
            limit=limit,
            offset=offset,
        )

        return cls(params=params)
