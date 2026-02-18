from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from spotantic.models import RequestModel


class GetAvailableMarketsRequest(RequestModel[None, None]):
    """Request model for Get Available Markets endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    endpoint: Optional[str] = "markets"
    """Endpoint associated with the request."""

    @classmethod
    def build(cls) -> GetAvailableMarketsRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Returns:
            Validated Request object.
        """
        return cls()
