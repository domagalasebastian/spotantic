from __future__ import annotations

from collections.abc import Sequence
from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer
from pydantic import field_validator

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemType


class CheckIfUserFollowsArtistsOrUsersRequestParams(BaseModel):
    """Params model for Check If User Follows Artists Or Users request."""

    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    item_type: SpotifyItemType = Field(serialization_alias="type")
    """The item type: artist or user."""

    item_ids: Annotated[
        Optional[Sequence[str]],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ] = None
    """A list of the Spotify IDs for the artists or users."""

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: SpotifyItemType) -> SpotifyItemType:
        """Validates that the type parameter is either artist or user.

        Args:
            value: The value to validate.

        Returns:
            The validated value.
        """
        if value not in (SpotifyItemType.ARTIST, SpotifyItemType.USER):
            raise ValueError("`type` parameter value is invalid!")

        return value


class CheckIfUserFollowsArtistsOrUsersRequest(RequestModel[CheckIfUserFollowsArtistsOrUsersRequestParams, None]):
    """Request model for Check If User Follows Artists Or Users endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_FOLLOW_READ}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/following/contains"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        item_type: SpotifyItemType,
        item_ids: Sequence[str],
    ) -> CheckIfUserFollowsArtistsOrUsersRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            item_type: The item type: artist or user.
            item_ids: A list of the Spotify IDs for the artists or users.

        Returns:
            Validated Request object.
        """
        params = CheckIfUserFollowsArtistsOrUsersRequestParams(
            item_type=item_type,
            item_ids=item_ids,
        )

        return cls(params=params)
