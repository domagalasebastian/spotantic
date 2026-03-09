from pydantic import BaseModel

from spotantic.models.spotify import TrackModel


class GetSeveralTracksResponse(BaseModel):
    """Response model for Get Several Tracks endpoint."""

    tracks: list[TrackModel]
    """List of tracks."""
