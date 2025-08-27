from typing import Optional
from typing import Sequence
from typing import Union

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.custom_types import SpotifyAlbumURI
from pyspotify.custom_types import SpotifyArtistURI
from pyspotify.custom_types import SpotifyPlaylistURI
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import StartResumePlaybackRequest
from pyspotify.models.player.requests import StartResumePlaybackRequestBody
from pyspotify.models.player.requests import StartResumePlaybackRequestParams
from pyspotify.models.player.requests._start_resume_playback import PositionOffsetModel
from pyspotify.models.player.requests._start_resume_playback import URIOffsetModel


async def start_resume_playback(
    client: PySpotifyClient,
    *,
    device_id: Optional[str] = None,
    context_uri: Optional[Union[SpotifyAlbumURI, SpotifyArtistURI, SpotifyPlaylistURI]] = None,
    uris: Optional[Sequence[SpotifyTrackURI]] = None,
    offset: Optional[Union[int, SpotifyTrackURI]] = None,
    position_ms: Optional[int] = None,
) -> APICallModel[StartResumePlaybackRequest, APIResponse, None]:
    if offset is None:
        offset_model = None
    elif isinstance(offset, int):
        offset_model = PositionOffsetModel(position=offset)
    else:
        offset_model = URIOffsetModel(uri=offset)

    request = StartResumePlaybackRequest(
        endpoint="me/player/play",
        params=StartResumePlaybackRequestParams(
            device_id=device_id,
        ),
        body=StartResumePlaybackRequestBody(
            context_uri=context_uri,
            uris=uris,
            offset=offset_model,
            position_ms=position_ms,
        ),
    )

    response = await client.request(request, empty_response=True)

    return APICallModel(request=request, response=response, data=None)
