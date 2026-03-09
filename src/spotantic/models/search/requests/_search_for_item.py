from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
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
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID

SUPPORTED_ITEM_TYPES = (
    SpotifyItemType.ALBUM,
    SpotifyItemType.ARTIST,
    SpotifyItemType.EPISODE,
    SpotifyItemType.PLAYLIST,
    SpotifyItemType.SHOW,
    SpotifyItemType.TRACK,
)


class SearchForItemIncludeExternal(str, Enum):
    """Allowed values for `include_external` attribute."""

    AUDIO = "audio"
    """It signals that the client can play externally hosted audio content,
    and marks the content as playable in the response."""


class SearchForItemRequestParams(BaseModel):
    """Params model for Search For Item request."""

    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    query: str = Field(serialization_alias="q")
    """Your search query."""

    item_type: Annotated[
        Sequence[SpotifyItemType],
        Field(serialization_alias="type"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of item types to search across. Search results include hits
    from all the specified item types."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""

    limit: Annotated[Optional[int], Field(ge=1, le=10)] = None
    """The maximum number of results to return in each item type."""

    offset: Annotated[Optional[int], Field(ge=0, le=1000)] = None
    """The index of the first result to return. Use with limit to get
    the next page of search results."""

    include_external: Optional[SearchForItemIncludeExternal] = None
    """If set to `audio`, it signals that the client can play
    externally hosted audio content, and marks the content as playable in the response."""

    @field_validator("item_type", mode="after")
    @classmethod
    def validate_type_param(cls, value: Sequence[SpotifyItemType]) -> Sequence[SpotifyItemType]:
        """Verifies that all of the specified item types are supported.

        The request supports only: albums, artists, playlists, tracks, shows,
        episodes or audiobooks.

        Args:
            value: The `item_type` provided by an user.

        Returns:
            Unchanged input value after validation.

        Raises:
            ValueError: If provided `item_type` contains unsupported types.
        """
        if any(item not in SUPPORTED_ITEM_TYPES for item in value):
            raise ValueError("`type` parameter value is invalid!")

        return value


class SearchForItemRequest(RequestModel[SearchForItemRequestParams, None]):
    """Request model for Search For Item endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "search"
    """Endpoint associated with the request."""

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
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            query: Your search query.
            item_type: A list of item types to search across. Search results include hits
              from all the specified item types.
            market: An ISO 3166-1 alpha-2 country code.
            limit: The maximum number of results to return in each item type.
            offset: The index of the first result to return. Use with limit to get
              the next page of search results.
            include_external: If set to `audio`, it signals that the client can play
              externally hosted audio content, and marks the content as playable in the response.

        Returns:
            Validated Request object.
        """
        params = SearchForItemRequestParams(
            query=query,
            item_type=item_type,
            market=market,
            limit=limit,
            offset=offset,
            include_external=include_external,
        )

        return cls(params=params)
