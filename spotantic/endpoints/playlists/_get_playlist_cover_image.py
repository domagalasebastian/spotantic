from spotantic._utils.models._type_validation import validate_is_instance_of
from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.playlists.requests import GetPlaylistCoverImageRequest
from spotantic.models.spotify import ImageModel
from spotantic.types import JsonAPIResponse
from spotantic.types import SpotifyItemID


async def get_playlist_cover_image(
    client: SpotanticClient,
    *,
    playlist_id: SpotifyItemID,
) -> APICallModel[GetPlaylistCoverImageRequest, JsonAPIResponse, list[ImageModel]]:
    """Get the current image associated with a specific playlist.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.
        playlist_id: The Spotify ID of the playlist.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetPlaylistCoverImageRequest.build(
        playlist_id=playlist_id,
    )
    response = await client.request_json(request)
    data = validate_is_instance_of(response, list[ImageModel])

    return APICallModel(request=request, response=response, data=data)
