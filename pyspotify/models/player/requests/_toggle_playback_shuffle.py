from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.custom_types import ParamsBool
from pyspotify.models import RequestModel


class TogglePlaybackShuffleRequestParams(BaseModel):
    state: ParamsBool
    device_id: Optional[str] = None


class TogglePlaybackShuffleRequest(RequestModel[TogglePlaybackShuffleRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.PUT
