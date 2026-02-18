from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from spotantic.models import RequestModel
from spotantic.types import AuthScope


class SeekToPositionRequestParams(BaseModel):
    """Params model for Seek To Position request."""

    position_ms: int
    """The position in milliseconds to seek to."""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class SeekToPositionRequest(RequestModel[SeekToPositionRequestParams, None]):
    """Request model for Seek To Position endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/seek"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        position_ms: int,
        device_id: Optional[str] = None,
    ) -> SeekToPositionRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            position_ms: The position in milliseconds to seek to.
            device_id: The id of the device this command is targeting.

        Returns:
            Validated Request object.
        """
        params = SeekToPositionRequestParams(
            position_ms=position_ms,
            device_id=device_id,
        )

        return cls(params=params)
