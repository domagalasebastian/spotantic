from http import HTTPMethod

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class GetPlaylistCoverImageRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)
    playlist_id: SpotifyItemID = Field(serialization_alias="id")


class GetPlaylistCoverImageRequest(RequestModel[GetPlaylistCoverImageRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
