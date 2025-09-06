from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import ChangePlaylistDetailsRequest
from pyspotify.models.playlists.requests import ChangePlaylistDetailsRequestBody
from pyspotify.models.playlists.requests import ChangePlaylistDetailsRequestParams


async def change_playlist_details(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    new_name: Optional[str] = None,
    new_public_flag: Optional[bool] = None,
    new_collaborative_flag: Optional[bool] = None,
    new_description: Optional[str] = None,
) -> APICallModel[ChangePlaylistDetailsRequest, APIResponse, None]:
    request = ChangePlaylistDetailsRequest(
        endpoint=f"playlists/{playlist_id}",
        params=ChangePlaylistDetailsRequestParams(
            playlist_id=playlist_id,
        ),
        body=ChangePlaylistDetailsRequestBody(
            name=new_name,
            public=new_public_flag,
            collaborative=new_collaborative_flag,
            description=new_description,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
