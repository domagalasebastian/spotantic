from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.custom_types import SpotifyLocaleID
from pyspotify.models import RequestModel


class GetSingleBrowseCategoryRequestParams(BaseModel):
    locale: Optional[SpotifyLocaleID] = None
    category_id: str


class GetSingleBrowseCategoryRequest(RequestModel[GetSingleBrowseCategoryRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
