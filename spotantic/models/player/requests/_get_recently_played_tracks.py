from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator

from spotantic.models import RequestModel
from spotantic.types import AuthScope


class GetRecentlyPlayedTracksRequestParams(BaseModel):
    """Params model for Get Recently Played Tracks request."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    after: Optional[int] = None
    """A Unix timestamp in milliseconds."""

    before: Optional[int] = None
    """A Unix timestamp in milliseconds."""

    @model_validator(mode="after")
    def check_only_cursor_is_given(self) -> GetRecentlyPlayedTracksRequestParams:
        """Validates that only one of `after` or `before` is provided.

        Returns:
            The validated model.

        Raises:
            ValueError: If both `after` and `before` are provided.
        """
        if self.after is not None and self.before is not None:
            raise ValueError("Specify either a before or after parameter, but not both!")

        return self


class GetRecentlyPlayedTracksRequest(RequestModel[GetRecentlyPlayedTracksRequestParams, None]):
    """Request model for Get Recently Played Tracks endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_RECENTLY_PLAYED}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/recently-played"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        limit: int = 20,
        after: Optional[int] = None,
        before: Optional[int] = None,
    ) -> GetRecentlyPlayedTracksRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            limit: The maximum number of items to return.
            after: A Unix timestamp in milliseconds.
            before: A Unix timestamp in milliseconds.

        Returns:
            Validated Request object.
        """
        params = GetRecentlyPlayedTracksRequestParams(limit=limit, after=after, before=before)

        return cls(params=params)
