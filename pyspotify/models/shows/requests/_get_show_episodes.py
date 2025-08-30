from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetShowEpisodesRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    show_id: SpotifyItemID = Field(serialization_alias="id")
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: int
    market: Optional[SpotifyMarketID] = None


class GetShowEpisodesRequest(RequestModel[GetShowEpisodesRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
