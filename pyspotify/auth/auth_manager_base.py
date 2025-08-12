from abc import ABC
from abc import abstractmethod

from pyspotify._utils.logger import logger

from .access_token_info import AccessTokenInfo
from .auth_settings import AuthSettings


class AuthManagerBase(ABC):
    def __init__(self, auth_settings: AuthSettings) -> None:
        self.__auth_settings = auth_settings
        self._logger = logger.getChild("auth")

    @property
    def auth_settings(self) -> AuthSettings:
        return self.__auth_settings

    @auth_settings.setter
    def auth_settings(self, value: AuthSettings) -> None:
        self.__auth_settings = value

    @abstractmethod
    async def authorize(self) -> AccessTokenInfo: ...


class RefreshableAuthManager(AuthManagerBase, ABC):
    @abstractmethod
    async def refresh(self, refresh_token: str) -> AccessTokenInfo: ...
