from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ._track_model import TrackModel
from .submodels import ContextModel


class PlayHistoryModel(BaseModel):
    """Model representing information about a play history."""

    track: TrackModel
    """The track the user listened to."""

    played_at: datetime
    """The date and time the track was played."""

    context: Optional[ContextModel] = None
    """The context the track was played from."""
