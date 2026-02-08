from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from pyspotify.models import RequestModel


class GetNewReleasesRequestParams(BaseModel):
    """Params model for Get New Releases request."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""


class GetNewReleasesRequest(RequestModel[GetNewReleasesRequestParams, None]):
    """Request model for Get New Releases endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "browse/new-releases"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        offset: int = 0,
    ) -> GetNewReleasesRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            limit: The maximum number of items to return.
            offset: The index of the first item to return.

        Returns:
            Validated Request object.
        """
        params = GetNewReleasesRequestParams(
            limit=limit,
            offset=offset,
        )

        return cls(params=params)
