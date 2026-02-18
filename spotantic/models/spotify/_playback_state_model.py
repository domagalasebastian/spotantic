from spotantic.types import RepeatMode

from ._currently_playing_item_model import CurrentlyPlayingItemModel
from ._device_model import DeviceModel


class PlaybackStateModel(CurrentlyPlayingItemModel):
    """Model representing the playback state."""

    device: DeviceModel
    """The device that is currently active."""

    repeat_state: RepeatMode
    """off, track, context"""

    shuffle_state: bool
    """If shuffle is on or off."""
