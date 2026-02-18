from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import GetPlaylistCoverImageRequest
from spotantic.models.spotify import ImageModel
from spotantic.types import APIResponse
from spotantic.types import SpotifyItemID


async def get_playlist_cover_image(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[GetPlaylistCoverImageRequest, APIResponse, list[ImageModel]]:
    """Get the cover image for a playlist.

    Get the current image associated with a specific playlist.

    Args:
        client: SpotanticClient instance.
        playlist_id: The Spotify ID of the playlist.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetPlaylistCoverImageRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request(request)
    assert response is not None
    data = [ImageModel(**image_data) for image_data in response]

    return APICallModel(request=request, response=response, data=data)
