from datetime import datetime
from datetime import timedelta
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl
from pydantic import field_validator

from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyItemURI
from pyspotify.models.spotify._episode_model import EpisodeModel
from pyspotify.models.spotify._track_model import TrackModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class ContextModel(BaseModel):
    context_type: SpotifyItemType = Field(alias="type")
    context_href: HttpUrl = Field(alias="href")
    external_urls: ExternalUrlsModel = Field(repr=False)
    context_uri: SpotifyItemURI = Field(alias="uri", repr=False)


class ActionModel(BaseModel):
    interrupting_playback: Optional[bool] = None
    pausing: Optional[bool] = None
    resuming: Optional[bool] = None
    seeking: Optional[bool] = None
    skipping_next: Optional[bool] = None
    skipping_prev: Optional[bool] = None
    toggling_repeat_context: Optional[bool] = None
    toggling_shuffle: Optional[bool] = None
    toggling_repeat_track: Optional[bool] = None
    transferring_playback: Optional[bool] = None


class CurrentlyPlayingItemModel(BaseModel):
    context: Optional[ContextModel] = None
    timestamp: datetime = Field(repr=False)
    progress: timedelta = Field(alias="progress_ms")
    is_playing: bool
    item: Optional[Union[TrackModel, EpisodeModel]] = Field(discriminator="item_type")
    currently_playing_type: Union[SpotifyItemType, Literal["unknown"]] = Field(repr=False)
    actions: ActionModel = Field(repr=False)

    @field_validator("progress", mode="before")
    def convert_progress_ms_to_timedelta(cls, value: int) -> timedelta:
        return timedelta(milliseconds=value)

    @field_validator("timestamp", mode="before")
    def convert_ms_timestamp_to_seconds(cls, value: int) -> int:
        return int(value / 1e3)
