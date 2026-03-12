from http import HTTPMethod

from spotantic.models.users.requests import GetUserProfileRequest
from spotantic.models.users.requests import GetUserProfileRequestParams


def test_get_user_profile_request():
    user_id = "user123"
    request = GetUserProfileRequest.build(user_id=user_id)

    assert request.endpoint == f"users/{user_id}"
    assert request.method_type is HTTPMethod.GET

    params = request.params
    assert isinstance(params, GetUserProfileRequestParams)
    assert params.user_id == user_id
    assert request.body is None
