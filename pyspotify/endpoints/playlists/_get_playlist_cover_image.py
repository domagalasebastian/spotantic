from typing import List

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import GetPlaylistCoverImageRequest
from pyspotify.models.spotify import ImageModel


async def get_playlist_cover_image(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[GetPlaylistCoverImageRequest, APIResponse, List[ImageModel]]:
    request = GetPlaylistCoverImageRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request)
    assert response is not None
    data = [ImageModel(**image_data) for image_data in response]

    return APICallModel(request=request, response=response, data=data)
