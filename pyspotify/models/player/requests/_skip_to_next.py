from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.models import RequestModel
from pyspotify.types import AuthScope


class SkipToNextRequestParams(BaseModel):
    """Params model for Skip To Next request."""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class SkipToNextRequest(RequestModel[SkipToNextRequestParams, None]):
    """Request model for Skip To Next endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.POST
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/next"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        device_id: Optional[str] = None,
    ) -> SkipToNextRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            device_id: The id of the device this command is targeting.

        Returns:
            Validated Request object.
        """
        params = SkipToNextRequestParams(
            device_id=device_id,
        )

        return cls(params=params)
