from datetime import datetime

from pydantic import BaseModel

from pyspotify.models.spotify._simplified_show_model import SimplifiedShowModel


class SavedShowModel(BaseModel):
    added_at: datetime
    show: SimplifiedShowModel
