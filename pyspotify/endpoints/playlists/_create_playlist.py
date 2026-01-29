from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import CreatePlaylistRequest
from pyspotify.models.spotify import PlaylistModel


async def create_playlist(
    client: PySpotifyClient,
    *,
    user_id: str,
    name: str,
    description: Optional[str] = None,
    public: Optional[bool] = None,
    collaborative: Optional[bool] = None,
) -> APICallModel[CreatePlaylistRequest, APIResponse, PlaylistModel]:
    """Create a playlist for a user.

    Create a playlist for a Spotify user. Each user is generally limited to a maximum of 11000 playlists.

    Args:
        client: PySpotifyClient instance.
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
    response = await client.request(request)
    assert response is not None
    data = PlaylistModel(**response)

    return APICallModel(request=request, response=response, data=data)
