from typing import Optional

from pydantic import Field

from spotantic.types import SpotifyMarketID

from ._user_model import UserModel
from .submodels import ExplicitContentModel


class CurrentUserModel(UserModel):
    """Model representing detailed profile information about the current user."""

    country: Optional[SpotifyMarketID] = Field(None, repr=False, deprecated=True)
    """The country of the user, as set in the user's account profile."""

    email: Optional[str] = Field(None, repr=False, deprecated=True)
    """The user's email address, as entered by the user when creating their account."""

    explicit_content: Optional[ExplicitContentModel] = Field(None, repr=False, deprecated=True)
    """The user's explicit content settings."""

    product: Optional[str] = Field(None, repr=False, deprecated=True)
    """The user's Spotify subscription level."""
