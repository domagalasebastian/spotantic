from http import HTTPMethod

from spotantic.models.users.requests import GetCurrentUserProfileRequest
from spotantic.types import AuthScope


def test_get_current_user_profile_request():
    request = GetCurrentUserProfileRequest.build()

    assert request.endpoint == "me"
    assert request.method_type is HTTPMethod.GET
    assert AuthScope.USER_READ_EMAIL in request.required_scopes
    assert AuthScope.USER_READ_PRIVATE in request.required_scopes
    assert request.params is None
    assert request.body is None
