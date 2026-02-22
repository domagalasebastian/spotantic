from pydantic import BaseModel

from spotantic.models.spotify import TrackModel


class GetArtistTopTracksResponse(BaseModel):
    """Response model for Get Artist Top Tracks endpoint."""

    tracks: list[TrackModel]
    """List of tracks."""
