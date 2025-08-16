from typing import Any
from typing import Optional

from pydantic import Json

from pyspotify.client import PySpotifyClient

__ENDPOINT_NAME = "markets"


async def get_available_markets(client: PySpotifyClient) -> Optional[Json[Any]]:
    return client.get(f"{__ENDPOINT_NAME}")
