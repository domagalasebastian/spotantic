from typing import Sequence

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

    external_ids: ExternalIdsModel = Field(repr=False)
    """Known external IDs for the album."""

    genres: Sequence[str] = Field(repr=False, deprecated="Deprecated: The array is always empty.")
    """A list of the genres the artist is associated with."""

    label: str
    """The label associated with the album."""

    popularity: int
    """The popularity of the album. The value will be between 0 and 100, with 100 being the most popular."""
