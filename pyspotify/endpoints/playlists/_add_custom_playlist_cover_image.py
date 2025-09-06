from typing import Optional

from pydantic import FilePath

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import AddCustomPlaylistCoverImageRequest
from pyspotify.models.playlists.requests import AddCustomPlaylistCoverImageRequestBody
from pyspotify.models.playlists.requests import AddCustomPlaylistCoverImageRequestParams


async def add_custom_playlist_cover_image(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    image_data: Optional[bytes] = None,
    file_path: Optional[FilePath] = None,
) -> APICallModel[AddCustomPlaylistCoverImageRequest, APIResponse, None]:
    request = AddCustomPlaylistCoverImageRequest(
        endpoint=f"playlists/{playlist_id}/images",
        params=AddCustomPlaylistCoverImageRequestParams(
            playlist_id=playlist_id,
        ),
        body=AddCustomPlaylistCoverImageRequestBody(
            image_data=image_data,
            file_path=file_path,
        ),
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
