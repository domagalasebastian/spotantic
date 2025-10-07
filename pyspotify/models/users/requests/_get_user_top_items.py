from __future__ import annotations

from enum import Enum
from http import HTTPMethod
from typing import Annotated
from typing import Set

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class GetUserTopItemsType(str, Enum):
    ARTISTS = "artists"
    TRACKS = "tracks"


class GetUserTopItemsTimeRange(str, Enum):
    SHORT_TERM = "short_term"
    MEDIUM_TERM = "medium_term"
    LONG_TERM = "long_term"


class GetUserTopItemsRequestParams(BaseModel):
    model_config = ConfigDict(use_enum_values=True, serialize_by_alias=True)

    item_type: GetUserTopItemsType = Field(serialization_alias="type")
    time_range: GetUserTopItemsTimeRange
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: Annotated[int, Field(ge=0)]


class GetUserTopItemsRequest(RequestModel[GetUserTopItemsRequestParams, None]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_READ_PRIVATE}
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(
        cls,
        *,
        item_type: GetUserTopItemsType,
        time_range: GetUserTopItemsTimeRange = GetUserTopItemsTimeRange.MEDIUM_TERM,
        limit: int = 20,
        offset: int = 0,
    ) -> GetUserTopItemsRequest:
        params = GetUserTopItemsRequestParams(item_type=item_type, time_range=time_range, limit=limit, offset=offset)
        endpoint = f"me/top/{item_type}"

        return cls(endpoint=endpoint, params=params)
