from __future__ import annotations

import asyncio
import atexit
from typing import Any
from typing import Dict
from typing import Optional

from aiohttp.client import ClientSession
from pydantic import Json

from pyspotify._utils.logger import logger
from pyspotify._utils.utils import drop_items_with_none_values

from .auth import AccessTokenInfo
from .auth._auth_manager_base import AuthManagerBase
from .auth._auth_manager_base import RefreshableAuthManager


class PySpotifyClient:
    __API_BASE = "https://api.spotify.com/v1/"

    def __init__(self, auth_manager: AuthManagerBase, access_token_info: AccessTokenInfo) -> None:
        self._logger = logger.getChild("client")
        self.__auth_manager = auth_manager
        self.__access_token_info = access_token_info
        self.__session = None
        atexit.register(lambda: asyncio.run(self.close_session()))

    @property
    def access_token_info(self) -> AccessTokenInfo:
        return self.__access_token_info

    async def setup_client_session(self) -> None:
        self._logger.info("Setting up new client session")
        headers = {
            "Authorization": f"{self.access_token_info.token_type} {self.access_token_info.access_token}",
        }

        # TODO: Add custom checker
        self.__session = ClientSession(base_url=self.__API_BASE, headers=headers)

    async def close_session(self) -> None:
        if self.__session is not None and not self.__session.closed:
            self._logger.info("Closing client session")
            await self.__session.close()

    async def refresh_access_token(self) -> None:
        refresh_token = self.access_token_info.refresh_token
        assert isinstance(
            self.__auth_manager, RefreshableAuthManager
        ), f"Cannot refresh access token with {type(self.__auth_manager)}"
        assert refresh_token is not None, "Refresh token was not provided!"

        await self.close_session()
        self.__access_token_info = await self.__auth_manager.refresh(refresh_token)
        await self.setup_client_session()

    async def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Optional[Json[Any]]:
        assert self.__session is not None, "Initialize session first!"
        if params is not None:
            params = drop_items_with_none_values(params)

        self._logger.debug(f"GET request with {url=} and {params=}")
        async with self.__session.get(url, params=params) as resp:
            assert resp.status == 200
            return await resp.json()

    async def put(
        self, url: str, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None
    ) -> Optional[Json[Any]]:
        assert self.__session is not None, "Initialize session first!"
        if params is not None:
            params = drop_items_with_none_values(params)

        if data is not None:
            data = drop_items_with_none_values(data)

        self._logger.debug(f"PUT request with {url=} and {params=}")
        async with self.__session.put(url, params=params, data=data) as resp:
            assert resp.status == 200
            return await resp.json()

    async def post(
        self, url: str, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None
    ) -> Optional[Json[Any]]:
        assert self.__session is not None, "Initialize session first!"
        if params is not None:
            params = drop_items_with_none_values(params)

        if data is not None:
            data = drop_items_with_none_values(data)

        self._logger.debug(f"POST request with {url=} and {params=}")
        async with self.__session.post(url, params=params, data=data) as resp:
            assert resp.status == 200
            return await resp.json()

    async def delete(self, url: str, params: Optional[Dict[str, Any]] = None) -> Optional[Json[Any]]:
        assert self.__session is not None, "Initialize session first!"
        if params is not None:
            params = drop_items_with_none_values(params)

        self._logger.debug(f"DELETE request with {url=} and {params=}")
        async with self.__session.delete(url, params=params) as resp:
            assert resp.status == 200
            return await resp.json()
