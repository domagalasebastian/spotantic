from pyspotify.custom_types import RepeatMode
from pyspotify.models.spotify._currently_playing_item_model import CurrentlyPlayingItemModel
from pyspotify.models.spotify._device_model import DeviceModel


class PlaybackStateModel(CurrentlyPlayingItemModel):
    device: DeviceModel
    repeat_state: RepeatMode
    shuffle_state: bool
