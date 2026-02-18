from datetime import datetime

from pydantic import BaseModel

from spotantic.models.spotify._simplified_show_model import SimplifiedShowModel


class SavedShowModel(BaseModel):
    """Model representing a show saved in the current Spotify user's library."""

    added_at: datetime
    """The date and time the episode was saved. Timestamps are returned in ISO 8601 format as
    Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ."""

    show: SimplifiedShowModel
    """Information about the show."""
