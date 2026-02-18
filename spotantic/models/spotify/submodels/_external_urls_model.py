from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl


class ExternalUrlsModel(BaseModel):
    """Model representing information about external URLs for an item."""

    spotify: Optional[HttpUrl] = None
    """The Spotify URL for the object."""
