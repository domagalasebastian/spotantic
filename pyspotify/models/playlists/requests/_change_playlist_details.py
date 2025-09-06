from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class ChangePlaylistDetailsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")


class ChangePlaylistDetailsRequestBody(BaseModel):
    name: Optional[str] = None
    public: Optional[bool] = None
    collaborative: Optional[bool] = None
    description: Optional[str] = None


class ChangePlaylistDetailsRequest(RequestModel[ChangePlaylistDetailsRequestParams, ChangePlaylistDetailsRequestBody]):
    method_type: HTTPMethod = HTTPMethod.PUT
