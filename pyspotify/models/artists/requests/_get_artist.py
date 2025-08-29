from http import HTTPMethod

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class GetArtistRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    artist_id: SpotifyItemID = Field(serialization_alias="id")


class GetArtistRequest(RequestModel[GetArtistRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
