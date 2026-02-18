from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator

from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType


class GetFollowedArtistsRequestParams(BaseModel):
    """Params model for Get Followed Artists request."""

    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    item_type: SpotifyItemType = Field(serialization_alias="type")
    """The item type."""

    after: Optional[SpotifyItemID] = None
    """The last artist ID retrieved from the previous request."""

    limit: Annotated[Optional[int], Field(ge=1, le=50)] = None
    """The maximum number of artists to return."""

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: SpotifyItemType) -> SpotifyItemType:
        """Validates that the type parameter is `artist`.

        Args:
            value: The value to validate.

        Returns:
            The validated value.
        """
        if value != SpotifyItemType.ARTIST:
            raise ValueError("`type` parameter value is invalid!")

        return value


class GetFollowedArtistsRequest(RequestModel[GetFollowedArtistsRequestParams, None]):
    """Request model for Get Followed Artists endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_FOLLOW_READ}
    """Required authorization scopes for the request."""

    endpoint: Optional[str] = "me/following"
    """Endpoint associated with the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        item_type: SpotifyItemType = SpotifyItemType.ARTIST,
        after: Optional[SpotifyItemID] = None,
        limit: Optional[int] = None,
    ) -> GetFollowedArtistsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            item_type: The item type.
            after: The last artist ID retrieved from the previous request.
            limit: The maximum number of artists to return.

        Returns:
            Validated Request object.
        """
        params = GetFollowedArtistsRequestParams(
            item_type=item_type,
            after=after,
            limit=limit,
        )

        return cls(params=params)
