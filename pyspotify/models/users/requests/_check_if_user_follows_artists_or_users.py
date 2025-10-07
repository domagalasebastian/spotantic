from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Set

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer
from pydantic import field_validator

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemType
from pyspotify.models import RequestModel


class CheckIfUserFollowsArtistsOrUsersRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    item_type: SpotifyItemType = Field(serialization_alias="type")
    item_ids: Annotated[
        Optional[Sequence[str]],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(lambda seq: ",".join(seq), return_type=str),
    ] = None

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: SpotifyItemType) -> SpotifyItemType:
        if value not in (SpotifyItemType.ARTIST, SpotifyItemType.USER):
            raise ValueError("`type` parameter value is invalid!")

        return value


class CheckIfUserFollowsArtistsOrUsersRequest(RequestModel[CheckIfUserFollowsArtistsOrUsersRequestParams, None]):
    required_scopes: Set[Scope] = {Scope.USER_FOLLOW_READ}
    method_type: HTTPMethod = HTTPMethod.GET
    endpoint: Optional[str] = "me/following/contains"

    @classmethod
    def build(
        cls,
        *,
        item_type: SpotifyItemType,
        item_ids: Sequence[str],
    ) -> CheckIfUserFollowsArtistsOrUsersRequest:
        params = CheckIfUserFollowsArtistsOrUsersRequestParams(
            item_type=item_type,
            item_ids=item_ids,
        )

        return cls(params=params)
