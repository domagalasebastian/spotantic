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


class SaveItemsToLibraryRequestParams(BaseModel):
    """Params model for Save Items to Library request."""

    uris: Annotated[
        Sequence[SpotifyItemURI],
        Field(max_length=40),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of the Spotify URIs for the items to be saved to the user's library."""


class SaveItemsToLibraryRequest(RequestModel[SaveItemsToLibraryRequestParams, None]):
    """Request model for Save Items to Library endpoint."""

    required_scopes: set[AuthScope] = {
        AuthScope.USER_LIBRARY_MODIFY,
        AuthScope.USER_FOLLOW_MODIFY,
        AuthScope.PLAYLIST_MODIFY_PUBLIC,
    }
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/library"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        uris: Sequence[SpotifyItemURI],
    ) -> SaveItemsToLibraryRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            uris: A list of the Spotify URIs for the items to be saved to the user's library.

        Returns:
            Validated Request object.
        """
        params = SaveItemsToLibraryRequestParams(
            uris=uris,
        )

        return cls(params=params)
