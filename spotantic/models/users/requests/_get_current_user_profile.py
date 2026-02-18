from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from spotantic.models import RequestModel
from spotantic.types import AuthScope


class GetCurrentUserProfileRequest(RequestModel[None, None]):
    """Request model for Get Current User Profile endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_READ_EMAIL, AuthScope.USER_READ_PRIVATE}
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
