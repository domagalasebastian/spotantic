from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from spotantic.models import RequestModel
from spotantic.types import AuthScope


class PausePlaybackRequestParams(BaseModel):
    """Params model for Pause Playback request."""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class PausePlaybackRequest(RequestModel[PausePlaybackRequestParams, None]):
    """Request model for Pause Playback endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/pause"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        device_id: Optional[str] = None,
    ) -> PausePlaybackRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            device_id: The id of the device this command is targeting.

        Returns:
            Validated Request object.
        """
        params = PausePlaybackRequestParams(device_id=device_id)

        return cls(params=params)
