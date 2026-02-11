from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import PlainSerializer

from pyspotify.models import RequestModel
from pyspotify.types import AuthScope


class TogglePlaybackShuffleRequestParams(BaseModel):
    """Params model for Toggle Playback Shuffle request."""

    state: Annotated[bool, PlainSerializer(lambda flag: str(flag).lower(), return_type=str)]
    """Whether to shuffle the playback or not."""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class TogglePlaybackShuffleRequest(RequestModel[TogglePlaybackShuffleRequestParams, None]):
    """Request model for Toggle Playback Shuffle endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/shuffle"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        state: bool,
        device_id: Optional[str] = None,
    ) -> TogglePlaybackShuffleRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            state: Whether to shuffle the playback or not.
            device_id: The id of the device this command is targeting.

        Returns:
            Validated Request object.
        """
        params = TogglePlaybackShuffleRequestParams(
            state=state,
            device_id=device_id,
        )

        return cls(params=params)
