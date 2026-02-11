from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.spotify import UserModel
from pyspotify.models.users.requests import GetUserProfileRequest
from pyspotify.types import APIResponse


async def get_user_profile(
    client: PySpotifyClient,
    *,
    user_id: str,
) -> APICallModel[GetUserProfileRequest, APIResponse, UserModel]:
    """Get public Spotify profile information for a Spotify user.

    Get public profile information about a Spotify user.

    Args:
        client: PySpotifyClient instance.
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
