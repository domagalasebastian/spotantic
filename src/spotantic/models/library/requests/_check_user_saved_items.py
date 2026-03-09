from __future__ import annotations

from collections.abc import Sequence
from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import PlainSerializer

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemURI


class CheckUserSavedItemsRequestParams(BaseModel):
    """Params model for Check User Saved Items request."""

    uris: Annotated[
        Sequence[SpotifyItemURI],
        Field(max_length=40),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify URIs for the items to check."""


class CheckUserSavedItemsRequest(RequestModel[CheckUserSavedItemsRequestParams, None]):
    """Request model for Check User Saved Items endpoint."""

    required_scopes: set[AuthScope] = {
        AuthScope.USER_LIBRARY_READ,
        AuthScope.USER_FOLLOW_READ,
        AuthScope.PLAYLIST_READ_PRIVATE,
    }
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/library/contains"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        uris: Sequence[SpotifyItemURI],
    ) -> CheckUserSavedItemsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            uris: A list of Spotify URIs for the items to check.

        Returns:
            Validated Request object.
        """
        params = CheckUserSavedItemsRequestParams(
            uris=uris,
        )

        return cls(params=params)
