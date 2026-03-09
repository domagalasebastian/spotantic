from pydantic import BaseModel

from spotantic.models.spotify import ArtistModel
from spotantic.models.spotify import PagedResultWithCursorsModel


class GetFollowedArtistsResponse(BaseModel):
    """Response model for Get Followed Artists endpoint."""

    artists: PagedResultWithCursorsModel[ArtistModel]
    """List of artists."""
