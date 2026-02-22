from pydantic import BaseModel

from spotantic.models.spotify import ArtistModel


class GetSeveralArtistsResponse(BaseModel):
    """Response model for Get Several Artists endpoint."""

    artists: list[ArtistModel]
    """List of artists."""
