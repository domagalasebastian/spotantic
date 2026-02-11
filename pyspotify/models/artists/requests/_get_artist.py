from __future__ import annotations

from http import HTTPMethod

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.models import RequestModel
from pyspotify.types import SpotifyItemID


class GetArtistRequestParams(BaseModel):
    """Params model for Get Artist request."""

    model_config = ConfigDict(serialize_by_alias=True)

    artist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the artist."""


class GetArtistRequest(RequestModel[GetArtistRequestParams, None]):
    """Request model for Get Artist endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        artist_id: SpotifyItemID,
    ) -> GetArtistRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            artist_id: The Spotify ID for the artist.

        Returns:
            Validated Request object.
        """
        params = GetArtistRequestParams(
            artist_id=artist_id,
        )

        endpoint = f"artists/{artist_id}"

        return cls(endpoint=endpoint, params=params)
