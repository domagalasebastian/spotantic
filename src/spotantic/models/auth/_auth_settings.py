from pathlib import Path
from typing import Optional
from typing import Union

from aiohttp import BasicAuth
from pydantic import FilePath
from pydantic import HttpUrl
from pydantic import NewPath
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AuthSettings(BaseSettings):
    """Model representing the authorization settings based on contents of `.env` file or env variables.

    The env variables shall start with `spotantic_auth_`. Mandatory variables depends on the authorization
    method.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="spotantic_auth_",
        extra="ignore",
    )

    client_id: Optional[SecretStr] = None
    """The Client ID generated after registering your application."""

    client_secret: Optional[SecretStr] = None
    """The Client Secret generated after registering your application."""

    redirect_uri: Optional[HttpUrl] = None
    """The URI to redirect to after the user grants or denies permission."""

    scope: Optional[str] = None
    """A space-separated list of scopes which have been granted for this access_token."""

    store_access_token: bool = False
    """If `True`, the access token information will be saved to `access_token_file_path` every time it is obtained."""

    access_token_file_path: Union[FilePath, NewPath] = Path(".token_info_cache")
    """File location to save the access token at."""

    def get_basic_auth(self) -> BasicAuth:
        """Create ``BasicAuth`` object for the current credentials.

        Returns:
            ``BasicAuth`` instance for current ``client_id`` and ``client_secret``.

        Raises:
            ValueError: If ``client_id`` or ``client_secret`` is unknown.
        """
        if self.client_id is None:
            raise ValueError("Client ID must be set to create `BasicAuth`")

        if self.client_secret is None:
            raise ValueError("Client Secret must be set to create `BasicAuth`")

        return BasicAuth(self.client_id.get_secret_value(), self.client_secret.get_secret_value())
