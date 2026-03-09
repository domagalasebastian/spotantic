from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl


class ArtistFollowersModel(BaseModel):
    """Model representing the information about the followers of the artist."""

    href: Optional[HttpUrl] = None
    """This will always be set to null, as the Web API does not support it at the moment."""

    total: int
    """The total number of followers."""
