from typing import Any
from typing import Optional

from pydantic import Json

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import BoundedInt1to50
from pyspotify.custom_types import SequenceMaxLen50
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID

__ENDPOINT_NAME = "episodes"


async def get_episode(
    client: PySpotifyClient, *, episode_id: SpotifyItemID, market: Optional[SpotifyMarketID] = None
) -> Optional[Json[Any]]:
    params = {
        "market": market,
    }

    return client.get(f"{__ENDPOINT_NAME}/{episode_id}", params=params)


async def get_several_episodes(
    client: PySpotifyClient, *, episode_ids: SequenceMaxLen50[SpotifyItemID], market: Optional[SpotifyMarketID] = None
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(episode_ids),
        "market": market,
    }

    return client.get(f"{__ENDPOINT_NAME}", params=params)


async def get_user_saved_episodes(
    client: PySpotifyClient, *, limit: BoundedInt1to50 = 20, offset: int = 0, market: Optional[SpotifyMarketID] = None
) -> Optional[Json[Any]]:
    params = {
        "limit": limit,
        "offset": offset,
        "market": market,
    }

    return client.get(f"me/{__ENDPOINT_NAME}", params=params)


async def save_episodes_for_current_user(
    client: PySpotifyClient, *, episode_ids: SequenceMaxLen50[SpotifyItemID]
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(episode_ids),
    }

    return client.put(f"me/{__ENDPOINT_NAME}", params=params)


async def remove_user_saved_episodes(
    client: PySpotifyClient, *, episode_ids: SequenceMaxLen50[SpotifyItemID]
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(episode_ids),
    }

    return client.delete(f"me/{__ENDPOINT_NAME}", params=params)


async def check_user_saved_episodes(
    client: PySpotifyClient, *, episode_ids: SequenceMaxLen50[SpotifyItemID]
) -> Optional[Json[Any]]:
    params = {
        "ids": ",".join(episode_ids),
    }

    return client.get(f"me/{__ENDPOINT_NAME}/contains", params=params)
