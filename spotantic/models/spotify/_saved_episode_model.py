from datetime import datetime

from pydantic import BaseModel

from ._episode_model import EpisodeModel


class SavedEpisodeModel(BaseModel):
    """Model representing an episode saved in the current Spotify user's library."""

    added_at: datetime
    """The date and time the episode was saved. Timestamps are returned in ISO 8601 format as
    Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ."""

    episode: EpisodeModel
    """Information about the episode."""
