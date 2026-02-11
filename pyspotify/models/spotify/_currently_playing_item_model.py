from datetime import datetime
from datetime import timedelta
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from pyspotify.types import SpotifyItemType

from ._episode_model import EpisodeModel
from ._track_model import TrackModel
from .submodels import ContextModel
from .submodels import PlaybackActionsModel


class CurrentlyPlayingItemModel(BaseModel):
    """Model representing the item currently being played on the user's Spotify account."""

    context: Optional[ContextModel] = None
    """A Context Object."""

    timestamp: datetime = Field(repr=False)
    """Unix Millisecond Timestamp when playback state was last changed."""

    progress: timedelta = Field(alias="progress_ms")
    """Progress into the currently playing track or episode."""

    is_playing: bool
    """`True` if something is currently playing."""

    item: Optional[Union[TrackModel, EpisodeModel]] = Field(discriminator="item_type")
    """The currently playing track or episode."""

    currently_playing_type: Union[SpotifyItemType, Literal["unknown"]] = Field(repr=False)
    """The object type of the currently playing item."""

    actions: PlaybackActionsModel = Field(repr=False)
    """Allows to update the user interface based on which playback actions are available within the current context."""

    @field_validator("progress", mode="before")
    def convert_progress_ms_to_timedelta(cls, value: int) -> timedelta:
        """Converts track/episode progress given in milliseconds to `timedelta` object.

        Args:
            value: Track/Episode progress [milliseconds].

        Returns:
            Track/Episode progress as `timedelta` object.
        """
        return timedelta(milliseconds=value)
