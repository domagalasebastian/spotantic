from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import UserModel
from spotantic.models.users.requests import GetUserProfileRequest
from spotantic.types import JsonAPIResponse


@deprecated("This endpoint is deprecated since 11 February 2026 for new users.")
async def get_user_profile(
    client: SpotanticClient,
    *,
    user_id: str,
) -> APICallModel[GetUserProfileRequest, JsonAPIResponse, UserModel]:
    """Get public profile information about a Spotify user.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        user_id: The Spotify user ID for the user.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserProfileRequest.build(user_id=user_id)
    response = await client.request_json(request)
    data = UserModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
