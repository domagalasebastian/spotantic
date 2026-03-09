from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl


class UserFollowersModel(BaseModel):
    """Model representing information about the followers of this user."""

    followers_href: Optional[HttpUrl] = Field(None, repr=False)
    """This will always be set to null, as the Web API does not support it at the moment."""

    total: int
    """The total number of followers."""
