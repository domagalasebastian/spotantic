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
from spotantic.types import SpotifyMarketID


class RemoveUserSavedShowsRequestParams(BaseModel):
    """Params model for Remove User Saved Shows request."""

    model_config = ConfigDict(serialize_by_alias=True)

    show_ids: Annotated[
        Sequence[SpotifyItemID],
        Field(max_length=50, serialization_alias="ids"),
        PlainSerializer(sequence_to_comma_separated_str, return_type=str),
    ]
    """A list of the Spotify IDs for the shows."""

    market: Optional[SpotifyMarketID] = None
    """An ISO 3166-1 alpha-2 country code."""


class RemoveUserSavedShowsRequest(RequestModel[RemoveUserSavedShowsRequestParams, None]):
    """Request model for Remove User Saved Shows endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_LIBRARY_MODIFY}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.DELETE
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/shows"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        show_ids: Sequence[SpotifyItemID],
        market: Optional[SpotifyMarketID] = None,
    ) -> RemoveUserSavedShowsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            show_ids: A list of the Spotify IDs for the shows.
            market: An ISO 3166-1 alpha-2 country code.

        Returns:
            Validated Request object.
        """
        params = RemoveUserSavedShowsRequestParams(
            show_ids=show_ids,
            market=market,
        )

        return cls(params=params)
