from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import UnfollowPlaylistRequest


async def unfollow_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[UnfollowPlaylistRequest, APIResponse, None]:
    """Unfollow a playlist on behalf of the current user.

    Remove the current user as a follower of a playlist.

    Args:
        client: An instance of `PySpotifyClient`.
        playlist_id: The Spotify ID of the playlist to unfollow.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = UnfollowPlaylistRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
