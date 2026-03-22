from collections.abc import Sequence
from datetime import timedelta
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl
from pydantic import field_validator

from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID
from spotantic.types import SpotifyTrackURI

from ._simplified_artist_model import SimplifiedArtistModel
from .submodels import ExternalUrlsModel
from .submodels import LinkedFromModel
from .submodels import RestrictionsModel


class SimplifiedTrackModel(BaseModel):
    """Model representing simplified Spotify catalog information for a single track."""

    model_config = ConfigDict(serialize_by_alias=True)

    artists: Sequence[SimplifiedArtistModel]
    """The artists who performed the track."""

    available_markets: Optional[Sequence[SpotifyMarketID]] = Field(None, repr=False, deprecated=True)
    """A list of the countries in which the track can be played, identified by their ISO 3166-1 alpha-2 code."""

    disc_number: int = Field(repr=False)
    """The disc number."""

    duration: timedelta = Field(alias="duration_ms")
    """The track length in milliseconds."""

    explicit: bool = Field(repr=False)
    """Whether or not the track has explicit lyrics."""

    external_urls: ExternalUrlsModel = Field(repr=False)
    """Known external URLs for this track."""

    track_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the track."""

    track_id: SpotifyItemID = Field(alias="id", repr=False)
    """The Spotify ID for the track."""

    is_playable: Optional[bool] = Field(None, repr=False)
    """Part of the response when Track Relinking is applied.
    If `True`, the track is playable in the given market. Otherwise `False`."""

    linked_from: Optional[LinkedFromModel] = Field(None, repr=False, deprecated=True)
    """Part of the response when Track Relinking is applied, and the requested track
    has been replaced with different track."""

    restrictions: Optional[RestrictionsModel] = Field(None, repr=False)
    """Included in the response when a content restriction is applied."""

    track_name: str = Field(alias="name")
    """The name of the track."""

    preview_url: Optional[str] = Field(None, repr=False, deprecated=True)
    """A link to a 30 second preview (MP3 format) of the track."""

    track_number: int = Field(repr=False)
    """The number of the track."""

    item_type: Literal["track"] = Field(alias="type", repr=False)
    """The item type."""

    track_uri: SpotifyTrackURI = Field(alias="uri", repr=False)
    """The Spotify URI for the track."""

    is_local: bool = Field(repr=False)
    """Whether or not the track is from a local file."""

    @field_validator("duration", mode="before")
    def convert_duration_ms_to_timedelta(cls, value: int) -> timedelta:
        """Converts track duration given in milliseconds to `timedelta` object.

        Args:
            value: Track duration [milliseconds].

        Returns:
            Track duration as `timedelta` object.
        """
        return timedelta(milliseconds=value)
