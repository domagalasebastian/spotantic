from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from pyspotify._utils.models import sequence_to_comma_separated_str
from pyspotify.models import RequestModel
from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyMarketID


class GetSeveralTracksRequestParams(BaseModel):
    """Params model for Get Several Tracks request."""

    model_config = ConfigDict(serialize_by_alias=True)

    track_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of the Spotify IDs for the tracks."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetSeveralTracksRequest(RequestModel[GetSeveralTracksRequestParams, None]):
    """Request model for Get Several Tracks endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "tracks"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        track_ids: Sequence[SpotifyItemID],
        market: Optional[SpotifyMarketID] = None,
    ) -> GetSeveralTracksRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            track_ids: A list of the Spotify IDs for the tracks.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetSeveralTracksRequestParams(
            track_ids=track_ids,
            market=market,
        )

        return cls(params=params)
