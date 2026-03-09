from __future__ import annotations

from collections.abc import Sequence
from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from spotantic._utils.models import sequence_to_comma_separated_str
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


class SaveEpisodesForCurrentUserRequestParams(BaseModel):
    """Params model for Save Episodes For Current User request."""

    model_config = ConfigDict(serialize_by_alias=True)

    episode_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of the Spotify IDs for the episodes to be saved to the user's library."""


class SaveEpisodesForCurrentUserRequest(RequestModel[SaveEpisodesForCurrentUserRequestParams, None]):
    """Request model for Save Episodes For Current User endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_LIBRARY_MODIFY}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/episodes"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        episode_ids: Sequence[SpotifyItemID],
    ) -> SaveEpisodesForCurrentUserRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            episode_ids: A list of the Spotify IDs for the episodes to be saved to the user's library.

        Returns:
            Validated Request object.
        """
        params = SaveEpisodesForCurrentUserRequestParams(
            episode_ids=episode_ids,
        )

        return cls(params=params)
