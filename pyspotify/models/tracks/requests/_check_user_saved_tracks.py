from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class CheckUserSavedTracksRequestParams(BaseModel):
    """Params model for Check User Saved Tracks request."""

    model_config = ConfigDict(serialize_by_alias=True)

    track_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(lambda seq: ",".join(seq), return_type=str),
    ]
    """A list of the Spotify IDs for the tracks."""


class CheckUserSavedTracksRequest(RequestModel[CheckUserSavedTracksRequestParams, None]):
    """Request model for Check User Saved Tracks endpoint."""

    required_scopes: set[Scope] = {Scope.USER_LIBRARY_READ}
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
