from datetime import datetime

from pydantic import BaseModel

from pyspotify.models.spotify._track_model import TrackModel


class SavedTrackModel(BaseModel):
    added_at: datetime
    track: TrackModel
