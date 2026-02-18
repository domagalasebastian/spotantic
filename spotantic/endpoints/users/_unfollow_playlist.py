from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import UnfollowPlaylistRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def unfollow_playlist(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[UnfollowPlaylistRequest, APIResponse, None]:
    """Unfollow a playlist on behalf of the current user.

    Remove the current user as a follower of a playlist.

    Args:
        client: An instance of `SpotanticClient`.
        playlist_id: The Spotify ID of the playlist to unfollow.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = UnfollowPlaylistRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
