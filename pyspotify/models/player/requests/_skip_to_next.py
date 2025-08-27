from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.models import RequestModel


class SkipToNextRequestParams(BaseModel):
    device_id: Optional[str] = None


class SkipToNextRequest(RequestModel[SkipToNextRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.POST
