from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyTrackURI

from ._external_urls_model import ExternalUrlsModel


class LinkedFromModel(BaseModel):
    """Model representing information about the Track Relinking."""

    model_config = ConfigDict(serialize_by_alias=True)

    external_urls: ExternalUrlsModel = Field(repr=False)
    """Known external URLs for this track."""

    track_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the track."""

    track_id: SpotifyItemID = Field(alias="id", repr=False)
    """The Spotify ID for the track."""

    item_type: Literal["track"] = Field(alias="type", repr=False)
    """The item type."""

    track_uri: SpotifyTrackURI = Field(alias="uri", repr=False)
    """The Spotify URI for the track."""
