from typing import Optional

from pydantic import Field

from pyspotify.custom_types import SpotifyMarketID

from ._user_model import UserModel
from .submodels import ExplicitContentModel
from .submodels import UserFollowersModel


class CurrentUserModel(UserModel):
    """Model representing detailed profile information about the current user."""

    country: Optional[SpotifyMarketID] = None
    """The country of the user, as set in the user's account profile."""

    email: Optional[str] = None
    """The user's email address, as entered by the user when creating their account."""

    explicit_content: Optional[ExplicitContentModel] = Field(None, repr=False)
    """The user's explicit content settings."""

    followers: UserFollowersModel
    """Information about the followers of the user."""

    product: Optional[str] = None
    """The user's Spotify subscription level."""
