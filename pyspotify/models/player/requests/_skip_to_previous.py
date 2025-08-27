from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.models import RequestModel


class SkipToPreviousRequestParams(BaseModel):
    device_id: Optional[str] = None


class SkipToPreviousRequest(RequestModel[SkipToPreviousRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.POST
