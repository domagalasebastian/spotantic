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
from pyspotify.models import RequestModel
from pyspotify.types import AuthScope
from pyspotify.types import SpotifyItemID


class CheckUserSavedAlbumsRequestParams(BaseModel):
    """Params model for Check User Saved Albums request."""

    model_config = ConfigDict(serialize_by_alias=True)

    album_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=20, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify IDs for the albums to check."""


class CheckUserSavedAlbumsRequest(RequestModel[CheckUserSavedAlbumsRequestParams, None]):
    """Request model for Check User Saved Albums endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_LIBRARY_READ}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/albums/contains"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        album_ids: Sequence[SpotifyItemID],
    ) -> CheckUserSavedAlbumsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            album_ids: A list of Spotify IDs for the albums to check.

        Returns:
            Validated Request object.
        """
        params = CheckUserSavedAlbumsRequestParams(
            album_ids=album_ids,
        )

        return cls(params=params)
