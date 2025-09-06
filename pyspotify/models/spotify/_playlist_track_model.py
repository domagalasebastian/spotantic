from datetime import datetime
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyUserURI
from pyspotify.models.spotify._episode_model import EpisodeModel
from pyspotify.models.spotify._track_model import TrackModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class AddedByModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)
    external_urls: ExternalUrlsModel = Field(repr=False)
    user_href: HttpUrl = Field(alias="href")
    user_id: str = Field(alias="id")
    item_type: Literal["user"] = Field(alias="type", repr=False)
    user_uri: SpotifyUserURI = Field(alias="uri", repr=False)


class PlaylistTrackModel(BaseModel):
    added_at: Optional[datetime] = None
    added_by: Optional[AddedByModel] = Field(None, repr=False)
    is_local: bool = Field(repr=False)
    track: Union[TrackModel, EpisodeModel] = Field(discriminator="item_type")
