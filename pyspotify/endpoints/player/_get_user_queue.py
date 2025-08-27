from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetUserQueueRequest
from pyspotify.models.spotify import UserQueueModel


async def get_user_queue(client: PySpotifyClient) -> APICallModel[GetUserQueueRequest, APIResponse, UserQueueModel]:
    request = GetUserQueueRequest(
        endpoint="me/player/queue",
    )

    response = await client.request(request)
    assert response is not None
    data = UserQueueModel(**response)

    return APICallModel(request=request, response=response, data=data)
