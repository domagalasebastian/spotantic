import asyncio

from pyspotify.auth import AuthCodeFlowManager
from pyspotify.client import PySpotifyClient
from pyspotify.models.auth import AuthSettings


async def create_pyspotify_client() -> PySpotifyClient:
    auth_settings = AuthSettings()
    auth_manager = AuthCodeFlowManager(auth_settings=auth_settings)

    await auth_manager.authorize()
    client = PySpotifyClient(auth_manager=auth_manager)

    return client


if __name__ == "__main__":
    asyncio.run(create_pyspotify_client())
