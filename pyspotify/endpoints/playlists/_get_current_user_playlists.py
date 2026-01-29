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
    """Get a list of the current user's playlists.

    Get a list of the playlists owned or followed by the current Spotify user.

    Args:
        client: PySpotifyClient instance.
        limit: The maximum number of playlists to return. Default is 20. Minimum is 1, maximum is 50.
        offset: The index of the first playlist to return. Default is 0.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetCurrentUserPlaylistsRequest.build(
        limit=limit,
        offset=offset,
    )
    response = await client.request(request)
    assert response is not None
    data = PagedResultModel[SimplifiedPlaylistModel](**response)

    return APICallModel(request=request, response=response, data=data)
