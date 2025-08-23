from datetime import datetime
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import Json

from pyspotify._utils.endpoints.request_params_validation import validate_request_params
from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import BoundedInt0to100
from pyspotify.custom_types import BoundedInt1to50
from pyspotify.custom_types import PlaybackSupportedItemType
from pyspotify.custom_types import RepeatMode
from pyspotify.custom_types import SequenceMaxLen1
from pyspotify.custom_types import SpotifyAlbumURI
from pyspotify.custom_types import SpotifyArtistURI
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.custom_types import SpotifyPlaylistURI
from pyspotify.custom_types import SpotifyTrackURI

__ENDPOINT_NAME = "player"


@validate_request_params
async def get_playback_state(
    client: PySpotifyClient,
    *,
    additional_types: Iterable[PlaybackSupportedItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> Optional[Json[Any]]:
    params = {
        "additional_types": ",".join(additional_types),
        "market": market,
    }

    return client.get(f"me/{__ENDPOINT_NAME}", params=params)


@validate_request_params
async def transfer_playback(
    client: PySpotifyClient, *, device_ids: SequenceMaxLen1[SpotifyItemID], play: Optional[bool] = None
) -> Optional[Json[Any]]:
    data = {
        "device_ids": list(device_ids),
        "play": play,
    }

    return client.put(f"me/{__ENDPOINT_NAME}", data=data)


@validate_request_params
async def get_available_devices(client: PySpotifyClient) -> Optional[Json[Any]]:
    return client.get(f"me/{__ENDPOINT_NAME}/devices")


@validate_request_params
async def get_currently_playing_track(
    client: PySpotifyClient,
    *,
    additional_types: Iterable[PlaybackSupportedItemType] = (SpotifyItemType.TRACK,),
    market: Optional[SpotifyMarketID] = None,
) -> Optional[Json[Any]]:
    params = {
        "additional_types": ",".join(additional_types),
        "market": market,
    }

    return client.get(f"me/{__ENDPOINT_NAME}/currently-playing", params=params)


@validate_request_params
async def start_resume_playback(
    client: PySpotifyClient,
    *,
    device_id: Optional[SpotifyItemID] = None,
    context_uri: Optional[Union[SpotifyAlbumURI, SpotifyArtistURI, SpotifyPlaylistURI]] = None,
    uris: Optional[Sequence[SpotifyTrackURI]] = None,
    offset: Optional[Union[int, SpotifyTrackURI]] = None,
    position_ms: Optional[int] = None,
) -> Optional[Json[Any]]:
    # TODO: Add params validation
    params = {
        "device_id": device_id,
    }

    data = {
        "context_uri": context_uri,
        "uris": uris,
        "offset": offset,
        "position_ms": position_ms,
    }

    return client.put(f"me/{__ENDPOINT_NAME}/play", params=params, data=data)


@validate_request_params
async def pause_playback(client: PySpotifyClient, *, device_id: Optional[SpotifyItemID] = None) -> Optional[Json[Any]]:
    params = {
        "device_id": device_id,
    }

    return client.put(f"me/{__ENDPOINT_NAME}/pause", params=params)


@validate_request_params
async def skip_to_next(client: PySpotifyClient, *, device_id: Optional[SpotifyItemID] = None) -> Optional[Json[Any]]:
    params = {
        "device_id": device_id,
    }

    return client.post(f"me/{__ENDPOINT_NAME}/next", params=params)


@validate_request_params
async def skip_to_previous(
    client: PySpotifyClient, *, device_id: Optional[SpotifyItemID] = None
) -> Optional[Json[Any]]:
    params = {
        "device_id": device_id,
    }

    return client.post(f"me/{__ENDPOINT_NAME}/previous", params=params)


@validate_request_params
async def seek_to_position(
    client: PySpotifyClient, *, position_ms: int, device_id: Optional[SpotifyItemID] = None
) -> Optional[Json[Any]]:
    params = {
        "position_ms": position_ms,
        "device_id": device_id,
    }

    return client.put(f"me/{__ENDPOINT_NAME}/seek", params=params)


@validate_request_params
async def set_repeat_mode(
    client: PySpotifyClient, *, state: RepeatMode, device_id: Optional[SpotifyItemID] = None
) -> Optional[Json[Any]]:
    params = {
        "state": state,
        "device_id": device_id,
    }

    return client.put(f"me/{__ENDPOINT_NAME}/repeat", params=params)


@validate_request_params
async def set_playback_volume(
    client: PySpotifyClient, *, volume_percent: BoundedInt0to100, device_id: Optional[SpotifyItemID] = None
) -> Optional[Json[Any]]:
    params = {
        "volume_percent": volume_percent,
        "device_id": device_id,
    }

    return client.put(f"me/{__ENDPOINT_NAME}/volume", params=params)


@validate_request_params
async def toggle_playback_shuffle(
    client: PySpotifyClient, *, state: bool, device_id: Optional[SpotifyItemID] = None
) -> Optional[Json[Any]]:
    params = {
        "state": state,
        "device_id": device_id,
    }

    return client.put(f"me/{__ENDPOINT_NAME}/shuffle", params=params)


@validate_request_params
async def get_recently_played_tracks(
    client: PySpotifyClient,
    *,
    limit: BoundedInt1to50,
    after: Optional[datetime] = None,
    before: Optional[datetime] = None,
) -> Optional[Json[Any]]:
    if after is not None and before is not None:
        raise ValueError("Specify either a before or after parameter, but not both!")

    params = {
        "limit": limit,
        "after": after,
        "before": before,
    }

    return client.get(f"me/{__ENDPOINT_NAME}/recently-played", params=params)


@validate_request_params
async def get_the_user_queue(client: PySpotifyClient) -> Optional[Json[Any]]:
    return client.get(f"me/{__ENDPOINT_NAME}/queue")


@validate_request_params
async def add_item_to_playback_queue(
    client: PySpotifyClient,
    *,
    uri: Union[SpotifyTrackURI, SpotifyEpisodeURI],
    device_id: Optional[SpotifyItemID] = None,
) -> Optional[Json[Any]]:
    params = {
        "uri": uri,
        "device_id": device_id,
    }

    return client.post(f"me/{__ENDPOINT_NAME}/queue", params=params)
