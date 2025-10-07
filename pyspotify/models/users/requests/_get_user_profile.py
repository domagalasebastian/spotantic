from __future__ import annotations

from http import HTTPMethod

from pydantic import BaseModel

from pyspotify.models import RequestModel


class GetUserProfileRequestParams(BaseModel):
    user_id: str


class GetUserProfileRequest(RequestModel[GetUserProfileRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(
        cls,
        *,
        user_id: str,
    ) -> GetUserProfileRequest:
        params = GetUserProfileRequestParams(user_id=user_id)
        endpoint = f"users/{user_id}"

        return cls(endpoint=endpoint, params=params)
