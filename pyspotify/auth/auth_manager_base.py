from abc import ABC, abstractmethod
import atexit
import asyncio
from typing import Optional

from pydantic.networks import HttpUrl
from pyspotify._utils.auth import AuthSettings
from aiohttp import ClientSession
from .access_token_info import AccessTokenInfo

class AuthManagerBase(ABC):
    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        scope: Optional[str] = None,
        env_file_path: Optional[str] = None,
    ) -> None:
        if env_file_path is not None:
            self.__auth_settings = AuthSettings(_env_file=env_file_path)
        else:
            self.__auth_settings = AuthSettings()
        
        self._store_access_token = self.__auth_settings.store_access_token
        self._access_token_file_path = self.__auth_settings.access_token_file_path
        self.__client_id = client_id or self.__auth_settings.client_id
        self.__client_secret = client_secret or self.__auth_settings.client_secret
        self.__redirect_uri = redirect_uri or self.__auth_settings.redirect_uri
        self.__scope = scope or self.__auth_settings.scope

    @property
    def client_id(self) -> Optional[str]:
        return self.__client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        self.__client_id = value

    @property
    def client_secret(self) -> Optional[str]:
        return self.__client_secret

    @client_secret.setter
    def client_secret(self, value: str) -> None:
        self.__client_secret = value

    @property
    def redirect_uri(self) -> Optional[str] | Optional[HttpUrl]:
        return self.__redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, value: str) -> None:
        self.__redirect_uri = value

    @property
    def scope(self) -> Optional[str]:
        return self.__scope

    @scope.setter
    def scope(self, value: str) -> None:
        self.__scope = value

    @abstractmethod
    async def authorize(self) -> AccessTokenInfo:
        ...

