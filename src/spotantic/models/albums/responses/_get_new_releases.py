from pydantic import BaseModel

from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedAlbumModel


class GetNewReleasesResponse(BaseModel):
    """Response model for Get New Releases endpoint."""

    albums: PagedResultModel[SimplifiedAlbumModel]
    """List of albums."""
