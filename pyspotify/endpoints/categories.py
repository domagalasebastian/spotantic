from typing import Any
from typing import Optional

from pydantic import Json

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import BoundedInt1to50
from pyspotify.custom_types import SpotifyLocaleID

__ENDPOINT_NAME = "categories"


async def get_several_browse_categories(
    client: PySpotifyClient, *, locale: Optional[SpotifyLocaleID] = None, limit: BoundedInt1to50 = 20, offset: int = 0
) -> Optional[Json[Any]]:
    params = {
        "locale": locale,
        "limit": limit,
        "offset": offset,
    }

    return client.get(f"browse/{__ENDPOINT_NAME}", params=params)


async def get_single_browse_categories(
    client: PySpotifyClient, *, category_id: str, locale: Optional[SpotifyLocaleID] = None
) -> Optional[Json[Any]]:
    params = {
        "locale": locale,
    }

    return client.get(f"browse/{__ENDPOINT_NAME}/{category_id}", params=params)
