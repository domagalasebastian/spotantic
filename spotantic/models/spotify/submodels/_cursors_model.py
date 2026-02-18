from typing import Optional

from pydantic import BaseModel


class CursorsModel(BaseModel):
    """Model representing the cursors used to find the next set of items."""

    after: Optional[str] = None
    """The cursor to use as key to find the next page of items."""

    before: Optional[str] = None
    """The cursor to use as key to find the previous page of items."""
