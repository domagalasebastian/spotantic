from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetUserSavedAlbumsRequestParams(BaseModel):
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: int
    market: Optional[SpotifyMarketID] = None


class GetUserSavedAlbumsRequest(RequestModel[GetUserSavedAlbumsRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
