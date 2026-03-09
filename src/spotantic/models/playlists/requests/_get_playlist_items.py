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
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


class GetPlaylistItemsRequestParams(BaseModel):
    """Params model for Get Playlist Items request."""

    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the playlist."""

    fields: Optional[str] = None
    """Filters for the response data."""

    limit: Annotated[int, Field(ge=1, le=50)]
    """The maximum number of items to return."""

    offset: int
    """The index of the first item to return."""

    additional_types: Annotated[
        Sequence[SpotifyItemType], PlainSerializer(sequence_to_comma_separated_str, return_type=str)
    ]
    """A list of item types to return."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""

    @field_validator("additional_types", mode="after")
    def check_value_is_playback_supported(cls, value: Sequence[SpotifyItemType]) -> Sequence[SpotifyItemType]:
        """Validates that the additional types are supported by playback.

        Args:
            value: The sequence of SpotifyItemType to validate.

        Returns:
            The validated sequence of SpotifyItemType.

        Raises:
            ValueError: If any item in the sequence is not supported by playback.
        """
        if any(item not in (SpotifyItemType.TRACK, SpotifyItemType.EPISODE) for item in value):
            raise ValueError(f"{value} is not valid item type supported by playback!")

        return value


class GetPlaylistItemsRequest(RequestModel[GetPlaylistItemsRequestParams, None]):
    """Request model for Get Playlist Items endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.PLAYLIST_READ_PRIVATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        fields: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
        additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
        market: Optional[SpotifyMarketID] = None,
    ) -> GetPlaylistItemsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist.
            fields: Filters for the response data.
            limit: The maximum number of items to return.
            offset: The index of the first item to return.
            additional_types: A list of item types to return.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetPlaylistItemsRequestParams(
            playlist_id=playlist_id,
            fields=fields,
            limit=limit,
            offset=offset,
            additional_types=additional_types,
            market=market,
        )
        endpoint = f"playlists/{playlist_id}/items"

        return cls(endpoint=endpoint, params=params)
