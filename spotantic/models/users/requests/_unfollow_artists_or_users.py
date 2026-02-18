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

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemType


class UnfollowArtistsOrUsersRequestParams(BaseModel):
    """Parameters for the Unfollow Artists or Users request model."""

    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    item_type: SpotifyItemType = Field(serialization_alias="type")
    """The type of the items to unfollow."""

    item_ids: Annotated[
        Optional[Sequence[str]],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ] = None
    """A sequence of Spotify IDs for the artists or users to unfollow."""

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: SpotifyItemType) -> SpotifyItemType:
        """Validate that the `type` parameter is either 'artist' or 'user'.

        Args:
            value: The SpotifyItemType value to validate.

        Returns:
            The validated SpotifyItemType value.
        """
        if value not in (SpotifyItemType.ARTIST, SpotifyItemType.USER):
            raise ValueError("`type` parameter value is invalid!")

        return value


class UnfollowArtistsOrUsersRequestBody(BaseModel):
    """Body for the Unfollow Artists or Users request model."""

    model_config = ConfigDict(serialize_by_alias=True)

    item_ids: Annotated[
        Optional[Sequence[str]],
        Field(max_length=50, serialization_alias="ids"),
    ] = None
    """A sequence of Spotify IDs for the artists or users to unfollow."""


class UnfollowArtistsOrUsersRequest(
    RequestModel[UnfollowArtistsOrUsersRequestParams, UnfollowArtistsOrUsersRequestBody]
):
    """Request model for Unfollow Artists or Users endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_FOLLOW_MODIFY}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.DELETE
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
    ) -> UnfollowArtistsOrUsersRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            item_type: The type of the items to unfollow.
            item_ids: A sequence of Spotify IDs for the artists or users to unfollow.

        Returns:
            Validated Request object.
        """
        params = UnfollowArtistsOrUsersRequestParams(
            item_type=item_type,
        )
        body = UnfollowArtistsOrUsersRequestBody(
            item_ids=item_ids,
        )

        return cls(params=params, body=body)
