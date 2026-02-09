from typing import Literal
from typing import Optional

from pydantic import BaseModel


class RestrictionsModel(BaseModel):
    """Model representing content restriction."""

    reason: Optional[Literal["market", "product", "explicit"]] = None
    """The reason for the restriction."""
