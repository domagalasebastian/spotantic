from collections.abc import Sequence
from datetime import datetime
from datetime import timedelta
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl
from pydantic import field_validator

from spotantic.types import SpotifyEpisodeURI
from spotantic.types import SpotifyItemID

from ._image_model import ImageModel
from .submodels import ExternalUrlsModel
from .submodels import RestrictionsModel
from .submodels import ResumePointModel


class SimplifiedEpisodeModel(BaseModel):
    """Model representing simplified Spotify catalog information for a single episode."""

    model_config = ConfigDict(serialize_by_alias=True)

    audio_preview_url: Optional[HttpUrl] = Field(None, repr=False, deprecated=True)
    """A URL to a 30 second preview (MP3 format) of the episode."""

    description: str
    """A description of the episode."""

    html_description: str = Field(repr=False)
    """A description of the episode. This field may contain HTML tags."""

    duration: timedelta = Field(alias="duration_ms")
    """The episode length in milliseconds."""

    explicit: bool = Field(repr=False)
    """Whether or not the episode has explicit content."""

    external_urls: ExternalUrlsModel = Field(repr=False)
    """External URLs for this episode."""

    episode_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the episode."""

    episode_id: SpotifyItemID = Field(alias="id")
    """The Spotify ID for the episode."""

    images: Sequence[ImageModel] = Field(repr=False)
    """The cover art for the episode in various sizes, widest first."""

    is_externally_hosted: bool = Field(repr=False)
    """`True` if the episode is hosted outside of Spotify's CDN."""

    is_playable: bool
    """`True` if the episode is playable in the given market. Otherwise `False`."""

    language: str = Field(
        repr=False,
        deprecated=(
            "This field is deprecated and might be removed in the future. Please use the languages field instead."
        ),
    )
    """The language used in the episode, identified by a ISO 639 code."""

    languages: Sequence[str]
    """A list of the languages used in the episode, identified by their ISO 639-1 code."""

    episode_name: str = Field(alias="name")
    """The name of the episode."""

    release_date: datetime
    """The date the episode was first released."""

    release_date_precision: Literal["year", "month", "day"] = Field(repr=False)
    """The precision with which `release_date` value is known."""

    resume_point: Optional[ResumePointModel] = Field(None, repr=False)
    """The user's most recent position in the episode"""

    item_type: Literal["episode"] = Field(alias="type", repr=False)
    """The item type."""

    episode_uri: SpotifyEpisodeURI = Field(alias="uri", repr=False)
    """The Spotify URI for the episode."""

    restrictions: Optional[RestrictionsModel] = Field(None, repr=False)
    """Included in the response when a content restriction is applied."""

    @field_validator("duration", mode="before")
    def convert_duration_ms_to_timedelta(cls, value: int) -> timedelta:
        """Converts episode duration given in milliseconds to `timedelta` object.

        Args:
            value: Episode duration [milliseconds].

        Returns:
            Episode duration as `timedelta` object.
        """
        return timedelta(milliseconds=value)
