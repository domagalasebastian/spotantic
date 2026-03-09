from typing import Optional

from pydantic import BaseModel


class PlaybackActionsModel(BaseModel):
    """Model representing information about playback actions that are available within the current context."""

    interrupting_playback: Optional[bool] = None
    """Interrupting playback."""

    pausing: Optional[bool] = None
    """Pausing."""

    resuming: Optional[bool] = None
    """Resuming."""

    seeking: Optional[bool] = None
    """Seeking playback location."""

    skipping_next: Optional[bool] = None
    """Skipping to the next context."""

    skipping_prev: Optional[bool] = None
    """Skipping to the previous context."""

    toggling_repeat_context: Optional[bool] = None
    """Toggling repeat context flag."""

    toggling_shuffle: Optional[bool] = None
    """Toggling shuffle flag."""

    toggling_repeat_track: Optional[bool] = None
    """Toggling repeat track flag."""

    transferring_playback: Optional[bool] = None
    """Transfering playback between devices."""
