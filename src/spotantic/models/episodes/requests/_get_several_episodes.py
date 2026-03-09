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
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


class GetSeveralEpisodesRequestParams(BaseModel):
    """Params model for Get Several Episodes request."""

    model_config = ConfigDict(serialize_by_alias=True)

    episode_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify episode IDs to retrieve."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetSeveralEpisodesRequest(RequestModel[GetSeveralEpisodesRequestParams, None]):
    """Request model for Get Several Episodes endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_PLAYBACK_POSITION}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "episodes"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        episode_ids: Sequence[SpotifyItemID],
        market: Optional[SpotifyMarketID] = None,
    ) -> GetSeveralEpisodesRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            episode_ids: A list of Spotify episode IDs to retrieve.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetSeveralEpisodesRequestParams(
            episode_ids=episode_ids,
            market=market,
        )

        return cls(params=params)
