from __future__ import annotations

from enum import Enum
from http import HTTPMethod
from typing import Annotated

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class GetUserTopItemsType(str, Enum):
    """The type of top items to retrieve."""

    ARTISTS = "artists"
    """The user's top artists."""

    TRACKS = "tracks"
    """The user's top tracks."""


class GetUserTopItemsTimeRange(str, Enum):
    """The time range over which to retrieve top items."""

    SHORT_TERM = "short_term"
    """Short-term. Approximately last 4 weeks."""

    MEDIUM_TERM = "medium_term"
    """Medium-term. Approximately last 6 months."""

    LONG_TERM = "long_term"
    """Long-term. ~1 year of data."""


class GetUserTopItemsRequestParams(BaseModel):
    """Params model for Get User Top Items request."""

    model_config = ConfigDict(use_enum_values=True, serialize_by_alias=True)

    item_type: GetUserTopItemsType = Field(serialization_alias="type")
    """The type of top items to retrieve."""

    time_range: GetUserTopItemsTimeRange
    """The time range over which to retrieve top items."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: Annotated[int, Field(ge=0)]
    """The index of the first item to return."""


class GetUserTopItemsRequest(RequestModel[GetUserTopItemsRequestParams, None]):
    """Request model for Get User Top Items endpoint."""

    required_scopes: set[Scope] = {Scope.PLAYLIST_READ_PRIVATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        item_type: GetUserTopItemsType,
        time_range: GetUserTopItemsTimeRange = GetUserTopItemsTimeRange.MEDIUM_TERM,
        limit: int = 20,
        offset: int = 0,
    ) -> GetUserTopItemsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            item_type: The type of top items to retrieve.
            time_range: The time range over which to retrieve top items.
            limit: The maximum number of items to return.
            offset: The index of the first item to return.

        Returns:
            Validated Request object.
        """
        params = GetUserTopItemsRequestParams(item_type=item_type, time_range=time_range, limit=limit, offset=offset)
        endpoint = f"me/top/{item_type}"

        return cls(endpoint=endpoint, params=params)
