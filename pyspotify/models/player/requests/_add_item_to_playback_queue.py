from http import HTTPMethod
from typing import Optional
from typing import Union

from pydantic import BaseModel

from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import RequestModel


class AddItemToPlaybackQueueRequestParams(BaseModel):
    uri: Union[SpotifyEpisodeURI, SpotifyTrackURI]
    device_id: Optional[str] = None


class AddItemToPlaybackQueueRequest(RequestModel[AddItemToPlaybackQueueRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.POST
