from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

from pyspotify.custom_types import RepeatMode
from pyspotify.models import RequestModel


class SetRepeatModeRequestParams(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    state: RepeatMode
    device_id: Optional[str] = None


class SetRepeatModeRequest(RequestModel[SetRepeatModeRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.PUT
