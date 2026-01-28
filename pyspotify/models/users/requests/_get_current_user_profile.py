from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class GetCurrentUserProfileRequest(RequestModel[None, None]):
    """Request model for Get Current User Profile endpoint."""

    required_scopes: set[Scope] = {Scope.USER_READ_EMAIL, Scope.USER_READ_PRIVATE}
    """Required authorization scopes for the request."""

    endpoint: Optional[str] = "me"
    """Endpoint associated with the request."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(cls) -> GetCurrentUserProfileRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Returns:
            Validated Request object.
        """
        return cls()
