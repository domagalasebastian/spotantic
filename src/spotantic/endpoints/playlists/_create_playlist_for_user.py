from typing import Optional

from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import CreatePlaylistForUserRequest
from spotantic.models.spotify import PlaylistModel
from spotantic.types import JsonAPIResponse


@deprecated("This endpoint is deprecated. Use Create Playlist instead.")
async def create_playlist_for_user(
    client: SpotanticClient,
    *,
    user_id: str,
    name: str,
    description: Optional[str] = None,
    public: Optional[bool] = None,
    collaborative: Optional[bool] = None,
) -> APICallModel[CreatePlaylistForUserRequest, JsonAPIResponse, PlaylistModel]:
    """Create a playlist for a Spotify user.

    Each user is generally limited to a maximum of 11000 playlists.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users. Existing users may be able to
       continue using it. More information on the deprecation can be found in the Spotify API documentation:
       `Update on Developer Access and Platform Security
       <https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security>`_.
       Use *Create Playlist* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        user_id: The Spotify user ID of the user.
        name: The name for the new playlist.
        description: The description for the new playlist.
        public: Whether the playlist should be public.
        collaborative: Whether the playlist should be collaborative.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CreatePlaylistForUserRequest.build(
        user_id=user_id,
        name=name,
        description=description,
        public=public,
        collaborative=collaborative,
    )
    response = await client.request_json(request)
    data = PlaylistModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
