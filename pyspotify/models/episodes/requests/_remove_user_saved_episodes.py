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


class RemoveUserSavedEpisodesRequestParams(BaseModel):
    """Params model for Remove User Saved Episodes request."""

    model_config = ConfigDict(serialize_by_alias=True)

    episode_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of Spotify IDs for the episodes to be removed from the user's library."""


class RemoveUserSavedEpisodesRequest(RequestModel[RemoveUserSavedEpisodesRequestParams, None]):
    """Request model for Remove User Saved Episodes endpoint."""

    required_scopes: set[Scope] = {Scope.USER_LIBRARY_MODIFY}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.DELETE
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/episodes"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        episode_ids: Sequence[SpotifyItemID],
    ) -> RemoveUserSavedEpisodesRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            episode_ids: A list of Spotify IDs for the episodes to be removed from the user's library.

        Returns:
            Validated Request object.
        """
        params = RemoveUserSavedEpisodesRequestParams(
            episode_ids=episode_ids,
        )

        return cls(params=params)
