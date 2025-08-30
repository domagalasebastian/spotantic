from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetShowRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    show_id: SpotifyItemID = Field(serialization_alias="id")
    market: Optional[SpotifyMarketID] = None


class GetShowRequest(RequestModel[GetShowRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
