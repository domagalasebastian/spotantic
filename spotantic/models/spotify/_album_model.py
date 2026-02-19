from collections.abc import Sequence
from typing import Optional

from pydantic import Field

from ._paged_result_model import PagedResultModel
from ._simplified_album_model import SimplifiedAlbumModel
from ._simplified_track_model import SimplifiedTrackModel
from .submodels import CopyrightModel
from .submodels import ExternalIdsModel


class AlbumModel(SimplifiedAlbumModel):
    """Model representing Spotify catalog information for a single album."""

    tracks: PagedResultModel[SimplifiedTrackModel]
    """The tracks of the album."""

    copyrights: Sequence[CopyrightModel] = Field(repr=False)
    """The copyright statements of the album."""

    external_ids: Optional[ExternalIdsModel] = Field(None, repr=False, deprecated=True)
    """Known external IDs for the album."""

    genres: Sequence[str] = Field(repr=False, deprecated="Deprecated: The array is always empty.")
    """A list of the genres the artist is associated with."""

    label: Optional[str] = Field(None, repr=False, deprecated=True)
    """The label associated with the album."""

    popularity: Optional[int] = Field(None, repr=False, deprecated=True)
    """The popularity of the album. The value will be between 0 and 100, with 100 being the most popular."""
