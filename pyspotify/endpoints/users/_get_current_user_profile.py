from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.spotify import CurrentUserModel
from pyspotify.models.users.requests import GetCurrentUserProfileRequest


async def get_current_user_profile(
    client: PySpotifyClient,
) -> APICallModel[GetCurrentUserProfileRequest, APIResponse, CurrentUserModel]:
    """Get the current Spotify user's profile information.

    Get detailed profile information about the current user (including the current user's username).

    Args:
        client: PySpotifyClient instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetCurrentUserProfileRequest.build()
    response = await client.request(request)
    assert response is not None
    data = CurrentUserModel(**response)

    return APICallModel(request=request, response=response, data=data)
