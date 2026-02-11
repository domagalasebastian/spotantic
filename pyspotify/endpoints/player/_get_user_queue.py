from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetUserQueueRequest
from pyspotify.models.player.responses import UserQueueModel
from pyspotify.types import APIResponse


async def get_user_queue(client: PySpotifyClient) -> APICallModel[GetUserQueueRequest, APIResponse, UserQueueModel]:
    """Get the user's queue.

    Get the list of objects that make up the user's queue.

    Args:
        client: PySpotifyClient instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserQueueRequest.build()
    response = await client.request(request)
    assert response is not None
    data = UserQueueModel(**response)

    return APICallModel(request=request, response=response, data=data)
