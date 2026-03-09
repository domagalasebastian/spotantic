from datetime import datetime

from pydantic import BaseModel

from ._track_model import TrackModel


class SavedTrackModel(BaseModel):
    """Model representing a track saved in the current Spotify user's 'Your Music' library."""

    added_at: datetime
    """The date and time the episode was saved. Timestamps are returned in ISO 8601 format as
    Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ."""

    track: TrackModel
    """Information about the track."""
