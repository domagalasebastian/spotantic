from pathlib import Path
from typing import Optional
from typing import Union

from pydantic import FilePath
from pydantic import HttpUrl
from pydantic import NewPath
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AuthSettings(BaseSettings):
    """Model representing the authorization settings based on contents of `.env` file or env variables.

    The env variables shall start with `pyspotify_auth_`. Mandatory variables depends on the authorization
    method.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="pyspotify_auth_",
        extra="ignore",
    )

    client_id: Optional[str] = None
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
