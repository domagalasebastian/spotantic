from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.users.requests import FollowPlaylistRequest


async def follow_playlist(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    public: bool = True,
) -> APICallModel[FollowPlaylistRequest, APIResponse, None]:
    request = FollowPlaylistRequest.build(
        playlist_id=playlist_id,
        public=public,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
