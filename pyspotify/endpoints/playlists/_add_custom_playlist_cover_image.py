from typing import Optional

from pydantic import FilePath

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import APICallModel
from pyspotify.models.playlists.requests import AddCustomPlaylistCoverImageRequest


async def add_custom_playlist_cover_image(
    client: PySpotifyClient,
    *,
    playlist_id: SpotifyItemID,
    image_data: Optional[bytes] = None,
    file_path: Optional[FilePath] = None,
) -> APICallModel[AddCustomPlaylistCoverImageRequest, APIResponse, None]:
    """Add a custom cover image to a playlist.

    Replace the image used to represent a specific playlist.

    Args:
        client: PySpotifyClient instance.
        playlist_id: The Spotify ID of the playlist.
        image_data: The image data as bytes. Must be a JPEG image, maximum size 256 KB.
        file_path: The file path to a JPEG image. Must be maximum size 256 KB.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = AddCustomPlaylistCoverImageRequest.build(
        playlist_id=playlist_id,
        image_data=image_data,
        file_path=file_path,
    )
    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
