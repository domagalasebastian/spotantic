from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyItemURI
from pyspotify.models.spotify._track_model import TrackModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class ContextModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    context_type: SpotifyItemType = Field(alias="type")
    context_href: HttpUrl = Field(alias="href")
    external_urls: ExternalUrlsModel = Field(repr=False)
    context_uri: SpotifyItemURI = Field(alias="uri", repr=False)


class PlayHistoryModel(BaseModel):
    track: TrackModel
    played_at: datetime
    context: Optional[ContextModel] = None
