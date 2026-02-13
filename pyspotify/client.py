from __future__ import annotations

from http import HTTPStatus
from typing import Literal

from aiohttp.client import ClientSession
from pydantic_core import from_json

from pyspotify._utils.logger import logger
from pyspotify.auth._auth_manager_base import AuthManagerBase
from pyspotify.models import RequestModel
from pyspotify.types import APIResponse


class PySpotifyClient:
    def __init__(self, auth_manager: AuthManagerBase) -> None:
        """Initialize the PySpotify client.

        Args:
            auth_manager: Authentication manager that manages the access token access info.
        """
        self._logger = logger.getChild("client")
        self.__auth_manager = auth_manager

    async def _get_authorization_header(self) -> dict[Literal["Authorization"], str]:
        """Return the `Authorization` header using the current valid access token.

        The header value is constructed as "{token_type} {access_token}".

        Raises:
            ValueError: If no access token is available.
        """
        access_token_info = await self.__auth_manager.get_valid_access_token()
        return {"Authorization": f"{access_token_info.token_type} {access_token_info.access_token}"}

    async def request(self, request: RequestModel, *, empty_response: bool = False) -> APIResponse:
        """Execute an HTTP request described by `request` and return parsed response.

        Args:
            request: `RequestModel` describing method, url, headers, params and body.
            empty_response: If true, return `None` without attempting to parse the body.

        Returns:
            Parsed API response or `None` for empty or unparsable responses.
        """

        self._logger.debug(f"Request: {request}")

        auth_header = await self._get_authorization_header()

        method = request.method_type
        url = str(request.url)
        headers = request.headers.model_dump(mode="json", exclude_none=True) | auth_header
        params = request.params.model_dump(mode="json", exclude_none=True) if request.params is not None else None
        data = request.body.model_dump_json(exclude_none=True) if request.body is not None else None

        async with ClientSession() as session:
            async with session.request(method=method, headers=headers, url=url, params=params, data=data) as resp:
                status = HTTPStatus(resp.status)
                self._logger.debug(f"Response status: {status}")

                response_data = await resp.read()
                response_data = response_data.strip()

        if not response_data:
            return None

        try:
            data = from_json(response_data)
        except ValueError:
            self._logger.debug(f"Response body (raw): {response_data}")
            self._logger.warning("Failed to deserialize response body as JSON; returning None.")
            return None

        return data
