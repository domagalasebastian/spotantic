from datetime import datetime

from pydantic import BaseModel

from ._album_model import AlbumModel


class SavedAlbumModel(BaseModel):
    """Model representing an album saved in the current Spotify user's 'Your Music' library."""

    added_at: datetime
    """The date and time the album was saved Timestamps are returned in ISO 8601 format as
    Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ"""

    album: AlbumModel
    """Information about the album."""
