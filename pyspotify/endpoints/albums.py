from typing import Any
from typing import Optional

from pydantic import Json

from pyspotify._utils.endpoints.request_params_validation import validate_request_params
from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import BoundedInt1to50
from pyspotify.custom_types import SequenceMaxLen20
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID

__ENDPOINT_NAME = "albums"


@validate_request_params
async def get_album(
    client: PySpotifyClient, *, album_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> Optional[Json[Any]]:
    params = {
        "market": market,
    }

    return await client.get(f"{__ENDPOINT_NAME}/{album_id}", params=params)


@validate_request_params
async def get_several_albums(
    client: PySpotifyClient, *, album_ids: SequenceMaxLen20[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(album_ids),
        "market": market,
    }

    return await client.get(f"{__ENDPOINT_NAME}", params=params)


@validate_request_params
async def get_album_tracks(
    client: PySpotifyClient,
    *,
    album_id: SpotifyItemID,
    limit: BoundedInt1to50 = 20,
    offset: int = 0,
    market: Optional[SpotifyMarketID] = None,
) -> Optional[Json[Any]]:
    params = {
        "limit": limit,
        "offset": offset,
        "market": market,
    }

    return await client.get(f"{__ENDPOINT_NAME}/{album_id}/tracks", params=params)


@validate_request_params
async def get_user_saved_albums(
    client: PySpotifyClient, *, limit: BoundedInt1to50 = 20, offset: int = 0, market: Optional[SpotifyMarketID] = None
) -> Optional[Json[Any]]:
    params = {
        "limit": limit,
        "offset": offset,
        "market": market,
    }

    return await client.get(f"me/{__ENDPOINT_NAME}", params=params)


@validate_request_params
async def save_albums_for_current_user(
    client: PySpotifyClient, *, album_ids: SequenceMaxLen20[SpotifyItemID]
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(album_ids),
    }

    return await client.put(f"me/{__ENDPOINT_NAME}", params=params)


@validate_request_params
async def remove_user_saved_albums(
    client: PySpotifyClient, *, album_ids: SequenceMaxLen20[SpotifyItemID]
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(album_ids),
    }

    return await client.delete(f"me/{__ENDPOINT_NAME}", params=params)


@validate_request_params
async def check_user_saved_albums(
    client: PySpotifyClient, *, album_ids: SequenceMaxLen20[SpotifyItemID]
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(album_ids),
    }

    return await client.get(f"me/{__ENDPOINT_NAME}/contains", params=params)


@validate_request_params
async def get_new_album_releases(
    client: PySpotifyClient, *, limit: BoundedInt1to50 = 20, offset: int = 0
) -> Optional[Json[Any]]:
    params = {
        "limit": limit,
        "offset": offset,
    }

    return await client.get("browse/new-releases", params=params)
