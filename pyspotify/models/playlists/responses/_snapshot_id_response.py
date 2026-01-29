from pydantic import BaseModel


class PlaylistSnapshotResponseModel(BaseModel):
    """Response model for playlist snapshot ID."""

    snapshot_id: str
    """The snapshot ID of the playlist."""
