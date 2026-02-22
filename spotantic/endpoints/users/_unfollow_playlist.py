from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import UnfollowPlaylistRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Remove Items from Library instead.")
async def unfollow_playlist(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[UnfollowPlaylistRequest, RawAPIResponse, None]:
    """Remove the current user as a follower of a playlist.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       Use *Remove Items from Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        playlist_id: The Spotify ID of the playlist to unfollow.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = UnfollowPlaylistRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
