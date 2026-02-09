from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer
from pydantic import field_validator

from pyspotify._utils.models import sequence_to_comma_separated_str
from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemType
from pyspotify.models import RequestHeadersModel
from pyspotify.models import RequestModel


class FollowArtistsOrUsersRequestParams(BaseModel):
    """Params model for Follow Artists Or Users request."""

    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    item_type: SpotifyItemType = Field(serialization_alias="type")
    """The type of item to follow."""

    item_ids: Annotated[
        Optional[Sequence[str]],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ] = None
    """A list of the Spotify IDs for the artists or users."""

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: SpotifyItemType) -> SpotifyItemType:
        """Validates that the type parameter is either `artist` or `user`.

        Args:
            value: The value to validate.

        Returns:
            The validated value.
        """
        if value not in (SpotifyItemType.ARTIST, SpotifyItemType.USER):
            raise ValueError("`type` should be either 'artist' or 'user'!")

        return value


class FollowArtistsOrUsersRequestBody(BaseModel):
    """Body model for Follow Artists Or Users request."""

    model_config = ConfigDict(serialize_by_alias=True)

    item_ids: Annotated[
        Optional[Sequence[str]],
        Field(max_length=50, serialization_alias="ids"),
    ] = None
    """A list of the Spotify IDs for the artists or users."""


class FollowArtistsOrUsersRequest(RequestModel[FollowArtistsOrUsersRequestParams, FollowArtistsOrUsersRequestBody]):
    """Request model for Follow Artists Or Users endpoint."""

    required_scopes: set[Scope] = {Scope.USER_FOLLOW_MODIFY}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/following"
    """Endpoint associated with the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        item_type: SpotifyItemType,
        item_ids: Sequence[str],
    ) -> FollowArtistsOrUsersRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            item_type: The type of item to follow.
            item_ids: A list of the Spotify IDs for the artists or users.

        Returns:
            Validated Request object.
        """
        params = FollowArtistsOrUsersRequestParams(
            item_type=item_type,
        )
        body = FollowArtistsOrUsersRequestBody(
            item_ids=item_ids,
        )

        return cls(params=params, body=body)
