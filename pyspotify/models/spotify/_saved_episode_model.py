from datetime import datetime

from pydantic import BaseModel

from pyspotify.models.spotify._episode_model import EpisodeModel


class SavedEpisodeModel(BaseModel):
    added_at: datetime
    episode: EpisodeModel
