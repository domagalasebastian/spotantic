import pytest

from spotantic.endpoints.users import get_current_user_profile
from spotantic.models.spotify import CurrentUserModel
from spotantic.models.users.requests import GetCurrentUserProfileRequest


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_current_user_profile(client):
    result = await get_current_user_profile(client)

    assert isinstance(result.request, GetCurrentUserProfileRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, CurrentUserModel)
