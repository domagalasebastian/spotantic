from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import GetUserPlaylistsRequest
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedPlaylistModel
from spotantic.types import JsonAPIResponse


@deprecated("This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).")
async def get_user_playlists(
    client: SpotanticClient,
    *,
    user_id: str,
    limit: int = 20,
    offset: int = 0,
) -> APICallModel[GetUserPlaylistsRequest, JsonAPIResponse, PagedResultModel[SimplifiedPlaylistModel]]:
    """Get a list of the playlists owned or followed by a Spotify user.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).

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
