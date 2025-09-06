from typing import Optional

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import CreatePlaylistRequest
from pyspotify.models.playlists.requests import CreatePlaylistRequestBody
from pyspotify.models.playlists.requests import CreatePlaylistRequestParams
from pyspotify.models.spotify import PlaylistModel


async def create_playlist(
    client: PySpotifyClient,
    *,
    user_id: str,
    name: str,
    description: Optional[str] = None,
    public: Optional[bool] = None,
    collaborative: Optional[bool] = None,
) -> APICallModel[CreatePlaylistRequest, APIResponse, PlaylistModel]:
    request = CreatePlaylistRequest(
        endpoint=f"users/{user_id}/playlists",
        params=CreatePlaylistRequestParams(
            user_id=user_id,
        ),
        body=CreatePlaylistRequestBody(
            name=name,
            public=public,
            collaborative=collaborative,
            description=description,
        ),
    )
    response = await client.request(request)
    assert response is not None
    data = PlaylistModel(**response)

    return APICallModel(request=request, response=response, data=data)
