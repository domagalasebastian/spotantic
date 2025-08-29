from __future__ import annotations

import asyncio
import atexit
from http import HTTPStatus

from aiohttp.client import ClientSession

from pyspotify._utils.logger import logger
from pyspotify.custom_types import APIResponse
from pyspotify.models import RequestModel

from .auth import AccessTokenInfo
from .auth._auth_manager_base import AuthManagerBase
from .auth._auth_manager_base import RefreshableAuthManager


class PySpotifyClient:
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
        self.__session = ClientSession(headers=headers, raise_for_status=True)

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

    async def request(self, request: RequestModel, *, empty_response: bool = False) -> APIResponse:
        assert self.__session is not None, "Initialize session first!"
        self._logger.debug(f"Request: {request}")
        method = request.method_type
        url = str(request.url)
        params = request.params.model_dump(exclude_none=True) if request.params is not None else None
        data = request.body.model_dump_json(exclude_none=True) if request.body is not None else None
        async with self.__session.request(method=method, url=url, params=params, data=data) as resp:
            status = resp.status
            self._logger.debug(f"Response status: {status}")
            if empty_response:
                # Temporary workaround for broken API endpoints which return some text data,
                # while documentation specifies that they are supposed to not return any data
                response_data = await resp.read()
                if status != HTTPStatus.NO_CONTENT:
                    self._logger.warning(f"Endpoint is supposed to not return any data, but the {response_data=}")

                return None

            content_type = "application/json" if status != HTTPStatus.NO_CONTENT else None
            return await resp.json(content_type=content_type)
