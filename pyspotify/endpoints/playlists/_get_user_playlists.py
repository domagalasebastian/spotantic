from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import GetUserPlaylistsRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedPlaylistModel


async def get_user_playlists(
    client: PySpotifyClient,
    *,
    user_id: str,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[GetUserPlaylistsRequest, APIResponse, PagedResultModel[SimplifiedPlaylistModel]]:
    request = GetUserPlaylistsRequest.build(
        user_id=user_id,
        limit=limit,
        offset=offset,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedPlaylistModel](**response)

    return APICallModel(request=request, response=response, data=data)
