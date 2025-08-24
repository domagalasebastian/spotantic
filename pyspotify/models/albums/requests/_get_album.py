from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetAlbumRequestParams(BaseModel):
    album_id: SpotifyItemID
    market: Optional[SpotifyMarketID] = None


class GetAlbumRequest(RequestModel[GetAlbumRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
