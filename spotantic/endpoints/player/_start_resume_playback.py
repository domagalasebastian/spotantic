from typing import Optional
from typing import Sequence
from typing import Union

from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import StartResumePlaybackRequest
from spotantic.types import APIResponse
from spotantic.types import SpotifyAlbumURI
from spotantic.types import SpotifyArtistURI
from spotantic.types import SpotifyPlaylistURI
from spotantic.types import SpotifyTrackURI


async def start_resume_playback(
    client: SpotanticClient,
    *,
    device_id: Optional[str] = None,
    context_uri: Optional[Union[SpotifyAlbumURI, SpotifyArtistURI, SpotifyPlaylistURI]] = None,
    uris: Optional[Sequence[SpotifyTrackURI]] = None,
    offset: Optional[Union[int, SpotifyTrackURI]] = None,
    position_ms: Optional[int] = None,
) -> APICallModel[StartResumePlaybackRequest, APIResponse, None]:
    """Start or resume the user's playback.

    Start a new context or resume current playback on the user's active device. This API only works for users
    who have Spotify Premium. The order of execution is not guaranteed when you use this API with
    other Player API endpoints.

    Args:
        client: SpotanticClient instance.
        device_id: The id of the device this command is targeting. If not supplied,
         the user's currently active device is the target.
        context_uri: Spotify URI of the context to play. Valid contexts are albums, artists, and playlists.
        uris: A list of Spotify track URIs to play.
        offset: Indicates from where in the context playback should start.
         If an integer is provided, it is treated as a position index in the context.
         If a Spotify track URI is provided, playback will start from that track.
        position_ms: Indicates the position in milliseconds to start playback.

    Returns:
        An object containing the request used to obtain the response and the response.
    """
    request = StartResumePlaybackRequest.build(
        device_id=device_id,
        context_uri=context_uri,
        uris=uris,
        offset=offset,
        position_ms=position_ms,
    )

    response = await client.request(request)

    return APICallModel(request=request, response=response, data=None)
