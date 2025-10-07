from __future__ import annotations

from http import HTTPMethod
from typing import Optional
from typing import Set

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class GetCurrentUserProfileRequest(RequestModel[None, None]):
    required_scopes: Set[Scope] = {Scope.USER_READ_EMAIL, Scope.USER_READ_PRIVATE}
    endpoint: Optional[str] = "me"
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(cls) -> GetCurrentUserProfileRequest:
        return cls()
