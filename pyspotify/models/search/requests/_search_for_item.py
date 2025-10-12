from __future__ import annotations

from enum import Enum
from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer
from pydantic import field_validator

from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel

SUPPORTED_ITEM_TYPES = (
    SpotifyItemType.ALBUM,
    SpotifyItemType.ARTIST,
    SpotifyItemType.EPISODE,
    SpotifyItemType.PLAYLIST,
    SpotifyItemType.SHOW,
    SpotifyItemType.TRACK,
)


class SearchForItemIncludeExternal(str, Enum):
    AUDIO = "audio"


class SearchForItemRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    query: str = Field(serialization_alias="q")
    item_type: Annotated[
        Sequence[SpotifyItemType],
        Field(serialization_alias="type"),
        PlainSerializer(lambda seq: ",".join(seq), return_type=str),
    ]
    market: Optional[SpotifyMarketID] = None
    limit: Annotated[Optional[int], Field(ge=1, le=50)] = None
    offset: Annotated[Optional[int], Field(ge=0, le=1000)] = None
    include_external: Optional[SearchForItemIncludeExternal] = None

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: Sequence[SpotifyItemType]) -> Sequence[SpotifyItemType]:
        if any(item not in SUPPORTED_ITEM_TYPES for item in value):
            raise ValueError("`type` parameter value is invalid!")

        return value


class SearchForItemRequest(RequestModel[SearchForItemRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
    endpoint: Optional[str] = "search"

    @classmethod
    def build(
        cls,
        *,
        query: str,
        item_type: Sequence[SpotifyItemType],
        market: Optional[SpotifyMarketID] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[SearchForItemIncludeExternal] = None,
    ) -> SearchForItemRequest:
        params = SearchForItemRequestParams(
            query=query,
            item_type=item_type,
            market=market,
            limit=limit,
            offset=offset,
            include_external=include_external,
        )

        return cls(params=params)
