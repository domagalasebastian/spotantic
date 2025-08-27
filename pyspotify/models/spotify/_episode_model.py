from datetime import datetime
from datetime import timedelta
from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl
from pydantic import field_validator

from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models.spotify._image_model import ImageModel
from pyspotify.models.spotify._show_model import ShowModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class RestrictionsModel(BaseModel):
    reason: Optional[Literal["market", "product", "explicit"]] = None


class ResumePointModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    fully_played: bool
    resume_position: timedelta = Field(alias="resume_position_ms")

    @field_validator("resume_position", mode="before")
    def convert_resume_position_ms_to_timedelta(cls, value: int) -> timedelta:
        return timedelta(milliseconds=value)


class EpisodeModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    audio_preview_url: Optional[HttpUrl] = Field(None, repr=False, deprecated=True)
    description: str
    html_description: str = Field(repr=False)
    duration: timedelta = Field(alias="duration_ms")
    explicit: bool = Field(repr=False)
    external_urls: ExternalUrlsModel = Field(repr=False)
    episode_href: HttpUrl = Field(alias="href")
    episode_id: SpotifyItemID = Field(alias="id")
    images: Sequence[ImageModel] = Field(repr=False)
    is_externally_hosted: bool = Field(repr=False)
    is_playable: bool
    language: str = Field(
        repr=False,
        deprecated=(
            "This field is deprecated and might be removed in the future. Please use the languages field instead."
        ),
    )
    languages: Sequence[str]
    release_date: datetime
    release_date_precision: Literal["year", "month", "day"] = Field(repr=False)
    resume_point: Optional[ResumePointModel] = Field(None, repr=False)
    item_type: Literal["episode"] = Field(alias="type", repr=False)
    episode_uri: SpotifyEpisodeURI = Field(alias="uri", repr=False)
    restrictions: Optional[RestrictionsModel] = Field(None, repr=False)
    show: ShowModel

    @field_validator("duration", mode="before")
    def convert_duration_ms_to_timedelta(cls, value: int) -> timedelta:
        return timedelta(milliseconds=value)
