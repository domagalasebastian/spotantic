from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from pyspotify.models import RequestModel


class SetPlaybackVolumeRequestParams(BaseModel):
    volume_percent: Annotated[int, Field(ge=0, le=100)]
    device_id: Optional[str] = None


class SetPlaybackVolumeRequest(RequestModel[SetPlaybackVolumeRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.PUT
