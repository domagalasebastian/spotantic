from __future__ import annotations

from collections.abc import Sequence
from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestModel
from spotantic.types import AlbumTypes
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


class GetArtistAlbumsRequestParams(BaseModel):
    """Params model for Get Artist Albums request."""

    model_config = ConfigDict(serialize_by_alias=True, use_enum_values=True)

    artist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the artist."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""

    include_groups: Annotated[
        Optional[Sequence[AlbumTypes]], PlainSerializer(sequence_to_comma_separated_str, return_type=str)
    ] = None
    """A list of keywords that will be used to filter the response."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetArtistAlbumsRequest(RequestModel[GetArtistAlbumsRequestParams, None]):
    """Request model for Get Artist Albums endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        artist_id: SpotifyItemID,
        limit: int = 20,
        offset: int = 0,
        market: Optional[SpotifyMarketID] = None,
        include_groups: Optional[Sequence[AlbumTypes]] = None,
    ) -> GetArtistAlbumsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            artist_id: The Spotify ID for the artist.
            limit: The maximum number of items to return.
            offset: The index of the first item to return.
            market: An ISO 3166-1 alpha-2 country code.
            include_groups: A list of keywords that will be used to filter the response.

        Returns:
            Validated Request object.
        """
        params = GetArtistAlbumsRequestParams(
            artist_id=artist_id,
            limit=limit,
            offset=offset,
            market=market,
            include_groups=include_groups,
        )

        endpoint = f"artists/{artist_id}/albums"

        return cls(endpoint=endpoint, params=params)
