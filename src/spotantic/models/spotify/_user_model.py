from collections.abc import Sequence
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from spotantic.types import SpotifyUserURI

from ._image_model import ImageModel
from .submodels import ExternalUrlsModel
from .submodels import FollowersModel


class UserModel(BaseModel):
    """Model representing public profile information about a Spotify user."""

    model_config = ConfigDict(serialize_by_alias=True)

    display_name: Optional[str] = None
    """The name displayed on the user's profile."""

    external_urls: ExternalUrlsModel = Field(repr=False)
    """Known external URLs for this user."""

    user_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint for this user."""

    user_id: str = Field(alias="id")
    """The Spotify user ID for the user."""

    images: Sequence[ImageModel] = Field(repr=False)
    """The user's profile image."""

    item_type: Literal["user"] = Field(alias="type", repr=False)
    """The item type."""

    user_uri: SpotifyUserURI = Field(alias="uri", repr=False)
    """The Spotify URI for the user."""

    followers: Optional[FollowersModel] = Field(None, repr=False, deprecated=True)
    """Information about the followers of the user."""
