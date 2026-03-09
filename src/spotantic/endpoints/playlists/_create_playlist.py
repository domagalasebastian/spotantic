from typing import Optional

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import CreatePlaylistRequest
from spotantic.models.spotify import PlaylistModel
from spotantic.types import JsonAPIResponse


async def create_playlist(
    client: SpotanticClient,
    *,
    user_id: str,
    name: str,
    description: Optional[str] = None,
    public: Optional[bool] = None,
    collaborative: Optional[bool] = None,
) -> APICallModel[CreatePlaylistRequest, JsonAPIResponse, PlaylistModel]:
    """Create a playlist for the current Spotify user.

    Each user is generally limited to a maximum of 11000 playlists.

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
    request = CreatePlaylistRequest.build(
        user_id=user_id,
        name=name,
        description=description,
        public=public,
        collaborative=collaborative,
    )
    response = await client.request_json(request)
    data = PlaylistModel.model_validate(response)

    return APICallModel(request=request, response=response, data=data)
