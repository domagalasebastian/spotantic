from pyspotify.client import PySpotifyClient
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import CheckIfCurrentUserFollowsPlaylistRequest
from pyspotify.types import APIResponse
from pyspotify.types import SpotifyItemID


async def check_if_current_user_follows_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[CheckIfCurrentUserFollowsPlaylistRequest, APIResponse, bool]:
    """Check if the current Spotify user follows a specific playlist.

    Check to see if the current user is following a specified playlist.

    Args:
        client: PySpotifyClient instance.
        playlist_id: The Spotify ID for the playlist.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = CheckIfCurrentUserFollowsPlaylistRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request)
    assert response is not None
    data = response[0]

    return APICallModel(request=request, response=response, data=data)
