from datetime import datetime
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field

from ._episode_model import EpisodeModel
from ._track_model import TrackModel
from .submodels import PlaylistOwnerModel


class PlaylistTrackModel(BaseModel):
    """Model representing full details of the items of a playlist owned by a Spotify user."""

    added_at: Optional[datetime] = None
    """The date and time the track or episode was added."""

    added_by: Optional[PlaylistOwnerModel] = Field(None, repr=False)
    """The Spotify user who added the track or episode."""

    is_local: bool = Field(repr=False)
    """Whether this track or episode is a local file or not."""

    track: Union[TrackModel, EpisodeModel] = Field(discriminator="item_type")
    """Information about the track or episode."""
