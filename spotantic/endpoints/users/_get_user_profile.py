from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import UserModel
from spotantic.models.users.requests import GetUserProfileRequest
from spotantic.types import APIResponse


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_user_profile(
    client: SpotanticClient,
    *,
    user_id: str,
) -> APICallModel[GetUserProfileRequest, APIResponse, UserModel]:
    """Get public profile information about a Spotify user.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
