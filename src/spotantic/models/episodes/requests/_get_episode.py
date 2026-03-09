from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID


class GetEpisodeRequestParams(BaseModel):
    """Params model for Get Episode request."""

    model_config = ConfigDict(serialize_by_alias=True)

    episode_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the episode."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetEpisodeRequest(RequestModel[GetEpisodeRequestParams, None]):
    """Request model for Get Episode endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_PLAYBACK_POSITION}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        episode_id: SpotifyItemID,
        market: Optional[SpotifyMarketID] = None,
    ) -> GetEpisodeRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            episode_id: The Spotify ID of the episode.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        endpoint = f"episodes/{episode_id}"

        params = GetEpisodeRequestParams(
            episode_id=episode_id,
            market=market,
        )

        return cls(endpoint=endpoint, params=params)
