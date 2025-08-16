from typing import Any
from typing import Iterable
from typing import Optional

from pydantic import Json

from pyspotify._utils.endpoints.request_params_validation import validate_request_params
from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import AlbumTypes
from pyspotify.custom_types import BoundedInt1to50
from pyspotify.custom_types import SequenceMaxLen50
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID

__ENDPOINT_NAME = "artists"


@validate_request_params
async def get_artist(client: PySpotifyClient, *, artist_id: SpotifyItemID) -> Optional[Json[Any]]:
    return client.get(f"{__ENDPOINT_NAME}/{artist_id}")


@validate_request_params
async def get_several_artists(
    client: PySpotifyClient, *, artist_ids: SequenceMaxLen50[SpotifyItemID]
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(artist_ids),
    }

    return client.get(f"{__ENDPOINT_NAME}", params=params)


@validate_request_params
async def get_artist_albums(
    client: PySpotifyClient,
    *,
    artist_id: SpotifyItemID,
    include_groups: Optional[Iterable[AlbumTypes]] = None,
    market: Optional[SpotifyMarketID] = None,
    limit: BoundedInt1to50 = 20,
    offset: int = 0,
) -> Optional[Json[Any]]:
    params = {
        "include_groups": ",".join(include_groups) if include_groups is not None else None,
        "market": market,
        "limit": limit,
        "offset": offset,
    }

    return client.get(f"{__ENDPOINT_NAME}/{artist_id}/albums", params=params)


@validate_request_params
async def get_artist_top_tracks(
    client: PySpotifyClient, *, artist_id: SpotifyItemID, market: Optional[SpotifyMarketID]
) -> Optional[Json[Any]]:
    params = {
        "market": market,
    }

    return client.get(f"{__ENDPOINT_NAME}/{artist_id}/top-tracks", params=params)
