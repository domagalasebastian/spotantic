from __future__ import annotations

import asyncio
import atexit
from typing import Any
from typing import Dict
from typing import Optional

from aiohttp.client import ClientSession

from .auth import AccessTokenInfo
from .auth import AuthManagerBase


class __PySpotifyClientMetaClass(type):
    __instance = None

    async def __call__(cls, *args, **kwargs) -> PySpotifyClient:
        if cls.__instance is None:
            cls.__instance = PySpotifyClient.__new__(cls)
            await cls.__instance.__init__(*args, **kwargs)

        return cls.__instance


class PySpotifyClient(metaclass=__PySpotifyClientMetaClass):
    __API_BASE = "https://api.spotify.com/v1/"

    async def __init__(
        self, auth: Optional[AuthManagerBase] = None, access_token_info: Optional[AccessTokenInfo] = None
    ) -> None:
        self.__auth = auth
        self.__access_token_info = access_token_info
        if self.__auth is None and self.__access_token_info is None:
            raise ValueError("Auth object or Access Token Info is required")

        if self.__access_token_info is None and self.__auth is not None:
            self.__access_token_info = await self.__auth.authorize()

        headers = {
            "Authorization": f"{self.__access_token_info.token_type} {self.__access_token_info.access_token}",
        }
        self.__session = ClientSession(base_url=self.__API_BASE, headers=headers)
        atexit.register(lambda: asyncio.run(self.__close_session()))

    async def __close_session(self) -> None:
        if not self.__session.closed:
            await self.__session.close()

    async def get(self, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if params is None:
            params = {}
        else:
            params = {k: v for k, v in params.items() if v is not None}

        async with self.__session.get(url, params=params) as resp:
            assert resp.status == 200
            return await resp.json()
