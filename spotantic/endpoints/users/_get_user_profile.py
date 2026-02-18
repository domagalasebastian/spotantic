from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import UserModel
from spotantic.models.users.requests import GetUserProfileRequest
from spotantic.types import APIResponse


async def get_user_profile(
    client: SpotanticClient,
    *,
    user_id: str,
) -> APICallModel[GetUserProfileRequest, APIResponse, UserModel]:
    """Get public Spotify profile information for a Spotify user.

    Get public profile information about a Spotify user.

    Args:
        client: SpotanticClient instance.
        user_id: The Spotify user ID for the user.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserProfileRequest.build(user_id=user_id)
    response = await client.request(request)
    assert response is not None
    data = UserModel(**response)

    return APICallModel(request=request, response=response, data=data)
