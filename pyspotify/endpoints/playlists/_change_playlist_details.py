from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import ChangePlaylistDetailsRequest


async def change_playlist_details(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    name: Optional[str] = None,
    public: Optional[bool] = None,
    collaborative: Optional[bool] = None,
    description: Optional[str] = None,
) -> APICallModel[ChangePlaylistDetailsRequest, APIResponse, None]:
    request = ChangePlaylistDetailsRequest.build(
        playlist_id=playlist_id,
        name=name,
        public=public,
        collaborative=collaborative,
        description=description,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
