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
    request = UnfollowPlaylistRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
