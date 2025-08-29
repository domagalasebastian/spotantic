from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetArtistTopTracksRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    artist_id: SpotifyItemID = Field(serialization_alias="id")
    market: Optional[SpotifyMarketID] = None


class GetArtistTopTracksRequest(RequestModel[GetArtistTopTracksRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
