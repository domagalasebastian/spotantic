from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from spotantic.types import SpotifyUserURI

from ._external_urls_model import ExternalUrlsModel


class PlaylistOwnerModel(BaseModel):
    """Model representing information about the user who owns the playlist."""

    model_config = ConfigDict(serialize_by_alias=True)

    external_urls: ExternalUrlsModel = Field(repr=False)
    """Known public external URLs for this user."""

    user_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint for this user."""

    user_id: str = Field(alias="id")
    """The Spotify user ID for this user."""

    item_type: Literal["user"] = Field(alias="type", repr=False)
    """The item type."""

    user_uri: SpotifyUserURI = Field(alias="uri", repr=False)
    """The Spotify URI for this user."""

    display_name: Optional[str] = None
    """The name displayed on the user's profile."""
