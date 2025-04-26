from typing import Optional

from aiohttp import BasicAuth
from aiohttp import ClientSession

from .access_token_info import AccessTokenInfo
from .auth_manager_base import AuthManagerBase


class ClientCredentialsFlowManager(AuthManagerBase):
    __TOKEN_URL = "https://accounts.spotify.com/api/token"

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        scope: Optional[str] = None,
        env_file_path: Optional[str] = None,
    ) -> None:
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            env_file_path=env_file_path,
        )

        assert self.client_id is not None, "Client ID must be set"
        assert self.client_secret is not None, "Client Secret must be set"

        self.__auth_header = BasicAuth(
            self.client_id,
            self.client_secret,
        )

    async def __get_access_token(self) -> AccessTokenInfo:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": "client_credentials",
        }

        async with ClientSession() as session:
            async with session.post(self.__TOKEN_URL, auth=self.__auth_header, headers=headers, data=data) as response:
                payload = await response.json()
                if response.status != 200:
                    raise Exception(f"Failed to get access token! Payload: {payload}")

            return AccessTokenInfo(**payload)

    async def authorize(self) -> AccessTokenInfo:
        token_info = await self.__get_access_token()

        if self._store_access_token:
            token_info.store_token(file_path=self._access_token_file_path)

        return token_info
