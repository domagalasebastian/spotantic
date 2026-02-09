from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from .submodels import CursorsModel


class PagedResultWithCursorsModel[ItemT: BaseModel](BaseModel):
    """Model representing the information about paged result with cursors used to find the next set of items."""

    model_config = ConfigDict(serialize_by_alias=True)

    href: HttpUrl
    """A link to the Web API endpoint returning the full result of the request."""

    limit: int
    """The maximum number of items in the response (as set in the query or by default)."""

    next_page: Optional[HttpUrl] = Field(None, alias="next")
    """URL to the next page of items."""

    cursors: CursorsModel
    """The cursors used to find the next set of items."""

    items: Sequence[ItemT]
    """An array of items collected from the current page."""
