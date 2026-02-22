import asyncio
from pathlib import Path

from spotantic.auth import AuthCodeFlowManager
from spotantic.auth import AuthCodePKCEFlowManager
from spotantic.auth import ClientCredentialsFlowManager
from spotantic.client import SpotanticClient
from spotantic.models.auth import AccessTokenInfo
from spotantic.models.auth import AuthSettings


async def auth_code_flow_client_setup() -> SpotanticClient:
    auth_settings = AuthSettings()
    auth_manager = AuthCodeFlowManager(auth_settings=auth_settings, allow_lazy_refresh=True)
    await auth_manager.authorize()

    return SpotanticClient(auth_manager=auth_manager, max_attempts=3, check_insufficient_scope=True)


async def auth_code_pkce_flow_client_setup() -> SpotanticClient:
    auth_settings = AuthSettings()
    auth_manager = AuthCodePKCEFlowManager(auth_settings=auth_settings, allow_lazy_refresh=True)
    await auth_manager.authorize()

    return SpotanticClient(auth_manager=auth_manager, max_attempts=3, check_insufficient_scope=True)


async def client_credentials_flow_client_setup() -> SpotanticClient:
    auth_settings = AuthSettings()
    auth_manager = ClientCredentialsFlowManager(auth_settings=auth_settings)
    await auth_manager.authorize()

    return SpotanticClient(auth_manager=auth_manager, max_attempts=3, check_insufficient_scope=True)


async def create_spotantic_client_with_existing_token() -> SpotanticClient:
    auth_settings = AuthSettings()
    token_info = AccessTokenInfo.load_token(Path(".token_info_cache"))
    auth_manager = AuthCodePKCEFlowManager(
        auth_settings=auth_settings, allow_lazy_refresh=True, access_token_info=token_info
    )

    return SpotanticClient(auth_manager=auth_manager, max_attempts=3, check_insufficient_scope=True)


if __name__ == "__main__":
    asyncio.run(create_spotantic_client_with_existing_token())
