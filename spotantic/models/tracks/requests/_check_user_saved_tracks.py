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
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


class CheckUserSavedTracksRequestParams(BaseModel):
    """Params model for Check User Saved Tracks request."""

    model_config = ConfigDict(serialize_by_alias=True)

    track_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of the Spotify IDs for the tracks."""


class CheckUserSavedTracksRequest(RequestModel[CheckUserSavedTracksRequestParams, None]):
    """Request model for Check User Saved Tracks endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_LIBRARY_READ}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/tracks/contains"
    """Endpoint associated with the request."""

    @classmethod
    def build(cls, *, track_ids: Sequence[SpotifyItemID]) -> CheckUserSavedTracksRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            track_ids: A list of the Spotify IDs for the tracks.

        Returns:
            Validated Request object.
        """
        params = CheckUserSavedTracksRequestParams(
            track_ids=track_ids,
        )

        return cls(params=params)
