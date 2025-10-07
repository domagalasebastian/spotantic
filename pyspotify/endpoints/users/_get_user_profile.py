from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.spotify import UserModel
from pyspotify.models.users.requests import GetUserProfileRequest


async def get_user_profile(
    client: PySpotifyClient,
    *,
    user_id: str,
) -> APICallModel[GetUserProfileRequest, APIResponse, UserModel]:
    request = GetUserProfileRequest.build(user_id=user_id)
    response = await client.request(request)
    assert response is not None
    data = UserModel(**response)

    return APICallModel(request=request, response=response, data=data)
