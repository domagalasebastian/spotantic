from __future__ import annotations

from collections.abc import Sequence
from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import PlainSerializer
from pydantic import field_validator

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemType
from spotantic.types import SpotifyMarketID


class GetCurrentlyPlayingTrackRequestParams(BaseModel):
    """Params model for Get Currently Playing Track request."""

    additional_types: Annotated[
        Sequence[SpotifyItemType], PlainSerializer(sequence_to_comma_separated_str, return_type=str)
    ]
    """A list of item types that your client supports besides the default track type."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""

    @field_validator("additional_types", mode="after")
    def check_value_is_playback_supported(cls, value: Sequence[SpotifyItemType]) -> Sequence[SpotifyItemType]:
        """Validates that the provided item types are supported by playback.

        Args:
            value: The sequence of Spotify item types to validate.

        Returns:
            The validated sequence of Spotify item types.

        Raises:
            ValueError: If any of the provided item types are not supported by playback.
        """
        if any(item not in (SpotifyItemType.TRACK, SpotifyItemType.EPISODE) for item in value):
            raise ValueError(f"{value} is not valid item type supported by playback!")

        return value


class GetCurrentlyPlayingTrackRequest(RequestModel[GetCurrentlyPlayingTrackRequestParams, None]):
    """Request model for Get Currently Playing Track endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_CURRENTLY_PLAYING}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/currently-playing"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
        market: Optional[SpotifyMarketID] = None,
    ) -> GetCurrentlyPlayingTrackRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            additional_types: A list of item types that your client supports besides the default track type.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetCurrentlyPlayingTrackRequestParams(
            additional_types=additional_types,
            market=market,
        )

        return cls(params=params)
