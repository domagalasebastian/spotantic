from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import GetUserQueueRequest
from spotantic.models.player.responses import GetUserQueueResponse
from spotantic.types import JsonAPIResponse


async def get_user_queue(
    client: SpotanticClient,
) -> APICallModel[GetUserQueueRequest, JsonAPIResponse, GetUserQueueResponse]:
    """Get the list of objects that make up the user's queue.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserQueueRequest.build()
    response = await client.request_json(request)
    data = GetUserQueueResponse.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
