import asyncio

from spotantic.auth import AuthCodeFlowManager
from spotantic.client import SpotanticClient
from spotantic.models.auth import AuthSettings


async def create_spotantic_client() -> SpotanticClient:
    auth_settings = AuthSettings()
    auth_manager = AuthCodeFlowManager(auth_settings=auth_settings)

    await auth_manager.authorize()
    client = SpotanticClient(auth_manager=auth_manager)

    return client


if __name__ == "__main__":
    asyncio.run(create_spotantic_client())
