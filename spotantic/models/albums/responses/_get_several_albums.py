from pydantic import BaseModel

from spotantic.models.spotify import AlbumModel


class GetSeveralAlbumsResponse(BaseModel):
    """Response model for Get Several Albums endpoint."""

    albums: list[AlbumModel]
    """List of albums."""
