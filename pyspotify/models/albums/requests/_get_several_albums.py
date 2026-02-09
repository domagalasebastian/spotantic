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
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetSeveralAlbumsRequestParams(BaseModel):
    """Params model for Get Several Albums request."""

    model_config = ConfigDict(serialize_by_alias=True)

    album_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=20, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify artist IDs to retrieve."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class GetSeveralAlbumsRequest(RequestModel[GetSeveralAlbumsRequestParams, None]):
    """Request model for Get Several Albums endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "albums"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        album_ids: Sequence[SpotifyItemID],
        market: Optional[SpotifyMarketID] = None,
    ) -> GetSeveralAlbumsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            album_ids: A list of Spotify artist IDs to retrieve.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = GetSeveralAlbumsRequestParams(
            album_ids=album_ids,
            market=market,
        )

        return cls(params=params)
