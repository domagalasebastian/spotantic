from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Set

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.models import RequestModel


class GetFollowedArtistsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    item_type: SpotifyItemType = Field(serialization_alias="type")
    after: Optional[SpotifyItemID] = None
    limit: Annotated[Optional[int], Field(ge=1, le=50)] = None

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: SpotifyItemType) -> SpotifyItemType:
        if value != SpotifyItemType.ARTIST:
            raise ValueError("`type` parameter value is invalid!")

        return value


class GetFollowedArtistsRequest(RequestModel[GetFollowedArtistsRequestParams, None]):
    required_scopes: Set[Scope] = {Scope.USER_FOLLOW_READ}
    endpoint: Optional[str] = "me/following"
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(
        cls,
        *,
        item_type: SpotifyItemType = SpotifyItemType.ARTIST,
        after: Optional[SpotifyItemID] = None,
        limit: Optional[int] = None,
    ) -> GetFollowedArtistsRequest:
        params = GetFollowedArtistsRequestParams(
            item_type=item_type,
            after=after,
            limit=limit,
        )

        return cls(params=params)
