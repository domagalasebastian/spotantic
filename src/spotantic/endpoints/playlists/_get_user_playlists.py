from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import GetUserPlaylistsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedPlaylistModel
from spotantic.types import JsonAPIResponse


@deprecated("This endpoint is deprecated since 11 February 2026 for new users.")
async def get_user_playlists(
    client: SpotanticClient,
    *,
    user_id: str,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[GetUserPlaylistsRequest, JsonAPIResponse, PagedResultModel[SimplifiedPlaylistModel]]:
    """Get a list of the playlists owned or followed by a Spotify user.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        user_id: The Spotify user ID of the user.
        limit: The maximum number of playlists to return. Default is 20. Minimum is 1, maximum is 50.
        offset: The index of the first playlist to return. Default is 0.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetUserPlaylistsRequest.build(
        user_id=user_id,
        limit=limit,
        offset=offset,
    )
    response = await client.request_json(request)
    data = PagedResultModel[SimplifiedPlaylistModel].model_validate(response)

    return APICallModel(request=request, response=response, data=data)
