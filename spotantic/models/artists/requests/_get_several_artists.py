from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestModel
from spotantic.types import SpotifyItemID


class GetSeveralArtistsRequestParams(BaseModel):
    """Params model for Get Several Artists request."""

    model_config = ConfigDict(serialize_by_alias=True)

    artist_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify artist IDs to retrieve."""


class GetSeveralArtistsRequest(RequestModel[GetSeveralArtistsRequestParams, None]):
    """Request model for Get Several Artists endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "artists"
    """Endpoint associated with the request."""

    @classmethod
    def build(cls, *, artist_ids: Sequence[SpotifyItemID]) -> GetSeveralArtistsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            artist_ids: A list of Spotify artist IDs to retrieve.

        Returns:
            Validated Request object.
        """
        params = GetSeveralArtistsRequestParams(
            artist_ids=artist_ids,
        )

        return cls(params=params)
