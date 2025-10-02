from pydantic import BaseModel


class PlaylistSnapshotResponseModel(BaseModel):
    snapshot_id: str
