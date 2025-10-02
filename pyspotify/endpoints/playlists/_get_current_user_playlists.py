from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import GetCurrentUserPlaylistsRequest
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedPlaylistModel


async def get_current_user_playlist(
    client: PySpotifyClient,
    *,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[GetCurrentUserPlaylistsRequest, APIResponse, PagedResultModel[SimplifiedPlaylistModel]]:
    request = GetCurrentUserPlaylistsRequest.build(
        limit=limit,
        offset=offset,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedPlaylistModel](**response)

    return APICallModel(request=request, response=response, data=data)
