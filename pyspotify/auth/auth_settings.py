from pathlib import Path
from typing import Optional
from typing import Union

from pydantic import FilePath
from pydantic import HttpUrl
from pydantic import NewPath
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="pyspotify_auth_",
        extra="ignore",
    )

    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    redirect_uri: Optional[HttpUrl] = None
    scope: Optional[str] = None
    store_access_token: bool = False
    access_token_file_path: Union[FilePath, NewPath] = Path(".token_info_cache")
