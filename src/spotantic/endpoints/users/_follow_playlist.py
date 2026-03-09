from typing_extensions import deprecated

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.users.requests import FollowPlaylistRequest
from spotantic.types import RawAPIResponse
from spotantic.types import SpotifyItemID


@deprecated("This endpoint is deprecated. Use Save Items to Library instead.")
async def follow_playlist(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
    public: bool = True,
) -> APICallModel[FollowPlaylistRequest, RawAPIResponse, None]:
    """Add the current user as a follower of a playlist.

    .. version-deprecated:: 0.1.0
       This endpoint is deprecated since 11 February 2026 for new users (March 9 2026 for old users).
       Use *Save Items to Library* instead.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
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
