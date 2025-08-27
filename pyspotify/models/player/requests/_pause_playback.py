from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.models import RequestModel


class PausePlaybackRequestParams(BaseModel):
    device_id: Optional[str] = None


class PausePlaybackRequest(RequestModel[PausePlaybackRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.PUT
