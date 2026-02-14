from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import FollowPlaylistRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def follow_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    public: bool = True,
) -> APICallModel[FollowPlaylistRequest, APIResponse, None]:
    """Follow a Spotify playlist.

    Add the current user as a follower of a playlist.

    Args:
        client: PySpotifyClient instance.
        playlist_id: The Spotify ID for the playlist to follow.
        public: If True the playlist will be included in the user's public playlists,
            if False it will be private. Default is True.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = FollowPlaylistRequest.build(
        playlist_id=playlist_id,
        public=public,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
