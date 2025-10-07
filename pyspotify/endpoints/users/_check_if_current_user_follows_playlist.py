from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import CheckIfCurrentUserFollowsPlaylistRequest


async def check_if_current_user_follows_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[CheckIfCurrentUserFollowsPlaylistRequest, APIResponse, bool]:
    request = CheckIfCurrentUserFollowsPlaylistRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request)
    assert response is not None
    data = response[0]

    return APICallModel(request=request, response=response, data=data)
