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


class CheckUserSavedEpisodesRequestParams(BaseModel):
    """Params model for Check User Saved Episodes request."""

    model_config = ConfigDict(serialize_by_alias=True)

    episode_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify episode IDs to check for."""


class CheckUserSavedEpisodesRequest(RequestModel[CheckUserSavedEpisodesRequestParams, None]):
    """Request model for Check User Saved Episodes endpoint."""

    required_scopes: set[Scope] = {Scope.USER_LIBRARY_READ}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/episodes/contains"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        episode_ids: Sequence[SpotifyItemID],
    ) -> CheckUserSavedEpisodesRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            episode_ids: A list of Spotify episode IDs to check for.

        Returns:
            Validated Request object.
        """
        params = CheckUserSavedEpisodesRequestParams(
            episode_ids=episode_ids,
        )

        return cls(params=params)
