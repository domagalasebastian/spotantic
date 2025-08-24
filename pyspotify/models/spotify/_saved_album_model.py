from datetime import datetime

from pydantic import BaseModel

from pyspotify.models.spotify._album_model import AlbumModel


class SavedAlbumModel(BaseModel):
    added_at: datetime
    album: AlbumModel
