from pydantic import BaseModel

from spotantic.models.spotify import SimplifiedShowModel


class GetSeveralShowsResponse(BaseModel):
    """Response model for Get Several Shows endpoint."""

    shows: list[SimplifiedShowModel]
    """List of shows."""
