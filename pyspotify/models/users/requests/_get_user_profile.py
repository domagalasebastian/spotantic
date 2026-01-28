from __future__ import annotations

from http import HTTPMethod

from pydantic import BaseModel

from pyspotify.models import RequestModel


class GetUserProfileRequestParams(BaseModel):
    """Params model for Get User Profile request."""

    user_id: str
    """The Spotify user ID of the user profile to retrieve."""


class GetUserProfileRequest(RequestModel[GetUserProfileRequestParams, None]):
    """Request model for Get User Profile endpoint."""

    method_type: HTTPMethod = HTTPMethod.GET
    """HTTP method for the request."""

    @classmethod
    def build(
        cls,
        *,
        user_id: str,
    ) -> GetUserProfileRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            user_id: The Spotify user ID of the user profile to retrieve.

        Returns:
            Validated Request object.
        """
        params = GetUserProfileRequestParams(user_id=user_id)
        endpoint = f"users/{user_id}"

        return cls(endpoint=endpoint, params=params)
