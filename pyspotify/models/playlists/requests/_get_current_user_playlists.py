from http import HTTPMethod
from typing import Annotated

from pydantic import BaseModel
from pydantic import Field

from pyspotify.models import RequestModel


class GetCurrentUserPlaylistsRequestParams(BaseModel):
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: int


class GetCurrentUserPlaylistsRequest(RequestModel[GetCurrentUserPlaylistsRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
