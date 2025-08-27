from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from pyspotify.custom_types import SpotifyLocaleID
from pyspotify.models import RequestModel


class GetSeveralBrowseCategoriesRequestParams(BaseModel):
    locale: Optional[SpotifyLocaleID] = None
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: int


class GetSeveralBrowseCategoriesRequest(RequestModel[GetSeveralBrowseCategoriesRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
