from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.models import RequestModel


class SeekToPositionRequestParams(BaseModel):
    position_ms: int
    device_id: Optional[str] = None


class SeekToPositionRequest(RequestModel[SeekToPositionRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.PUT
