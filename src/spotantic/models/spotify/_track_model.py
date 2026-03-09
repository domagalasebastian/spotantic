from typing import Optional

from pydantic import Field

from ._simplified_album_model import SimplifiedAlbumModel
from ._simplified_track_model import SimplifiedTrackModel
from .submodels import ExternalIdsModel


class TrackModel(SimplifiedTrackModel):
    """Model representing Spotify catalog information for a single track identified by its unique Spotify ID."""

    album: SimplifiedAlbumModel
    """The album on which the track appears."""

    external_ids: Optional[ExternalIdsModel] = Field(None, repr=False, deprecated=True)
    """Known external IDs for the track."""

    popularity: Optional[int] = Field(None, repr=False, deprecated=True)
    """The popularity of the track."""
