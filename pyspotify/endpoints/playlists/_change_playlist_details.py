from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import ChangePlaylistDetailsRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def change_playlist_details(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    name: Optional[str] = None,
    public: Optional[bool] = None,
    collaborative: Optional[bool] = None,
    description: Optional[str] = None,
) -> APICallModel[ChangePlaylistDetailsRequest, APIResponse, None]:
    """Change playlist details.

    Change a playlist's name and public/private state.

    Args:
        client: PySpotifyClient instance.
        playlist_id: The Spotify ID of the playlist.
        name: The new name for the playlist.
        public: Whether the playlist should be public.
        collaborative: Whether the playlist should be collaborative.
        description: The new description for the playlist.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = ChangePlaylistDetailsRequest.build(
        playlist_id=playlist_id,
        name=name,
        public=public,
        collaborative=collaborative,
        description=description,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
