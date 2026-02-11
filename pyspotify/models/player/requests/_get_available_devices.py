from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pyspotify.models import RequestModel
from pyspotify.types import AuthScope


class GetAvailableDevicesRequest(RequestModel[None, None]):
    """Request model for Get Available Devices endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/devices"
    """Endpoint associated with the request."""

    @classmethod
    def build(cls) -> GetAvailableDevicesRequest:
        """Builds a request model.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Returns:
            Validated Request object.
        """
        return cls()
