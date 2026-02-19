from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import CheckIfCurrentUserFollowsPlaylistRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Check User's Saved Items instead.")
async def check_if_current_user_follows_playlist(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[CheckIfCurrentUserFollowsPlaylistRequest, APIResponse, bool]:
    """Check to see if the current user is following a specified playlist.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       This endpoint is deprecated. Use *Check User's Saved Items* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
