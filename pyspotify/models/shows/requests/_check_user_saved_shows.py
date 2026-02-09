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
from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class CheckUserSavedShowsRequestParams(BaseModel):
    """Params model for Check User Saved Shows request."""

    model_config = ConfigDict(serialize_by_alias=True)

    show_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of the Spotify IDs for the shows."""


class CheckUserSavedShowsRequest(RequestModel[CheckUserSavedShowsRequestParams, None]):
    """Request model for Check User Saved Shows endpoint."""

    required_scopes: set[Scope] = {Scope.USER_LIBRARY_READ}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/shows/contains"
    """Endpoint associated with the request."""

    @classmethod
    def build(cls, *, show_ids: Sequence[SpotifyItemID]) -> CheckUserSavedShowsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            show_ids: A list of the Spotify IDs for the shows.

        Returns:
            Validated Request object.
        """
        params = CheckUserSavedShowsRequestParams(
            show_ids=show_ids,
        )

        return cls(params=params)
