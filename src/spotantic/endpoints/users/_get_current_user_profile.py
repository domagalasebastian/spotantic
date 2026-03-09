from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.spotify import CurrentUserModel
from spotantic.models.users.requests import GetCurrentUserProfileRequest
from spotantic.types import JsonAPIResponse


async def get_current_user_profile(
    client: SpotanticClient,
) -> APICallModel[GetCurrentUserProfileRequest, JsonAPIResponse, CurrentUserModel]:
    """Get detailed profile information about the current user (including the current user's username).

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetCurrentUserProfileRequest.build()
    response = await client.request_json(request)
    data = CurrentUserModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
