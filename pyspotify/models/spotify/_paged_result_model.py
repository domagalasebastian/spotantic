from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl


class PagedResultModel[ItemT: BaseModel](BaseModel):
    """Model representing the information about paged result."""

    model_config = ConfigDict(serialize_by_alias=True)

    href: HttpUrl
    """A link to the Web API endpoint returning the full result of the request."""

    limit: int
    """The maximum number of items in the response (as set in the query or by default)."""

    next_page: Optional[HttpUrl] = Field(None, alias="next")
    """URL to the next page of items."""

    offset: int
    """The offset of the items returned (as set in the query or by default)."""

    previous_page: Optional[HttpUrl] = Field(None, alias="previous")
    """URL to the previous page of items."""

    total: int
    """The total number of items available to return."""

    items: Sequence[ItemT]
    """An array of items collected from the current page."""
