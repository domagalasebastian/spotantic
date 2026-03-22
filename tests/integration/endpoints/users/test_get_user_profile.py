import pytest

from spotantic.endpoints.users import get_user_profile
from spotantic.models.spotify import UserModel
from spotantic.models.users.requests import GetUserProfileRequest
from spotantic.types import SpotifyItemType


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_user_profile(client, example_spotify_item_id):
    result = await get_user_profile(client, user_id=example_spotify_item_id[SpotifyItemType.USER])

    assert isinstance(result.request, GetUserProfileRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, UserModel)
