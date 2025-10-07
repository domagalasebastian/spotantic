from typing import Optional
from typing import Sequence
from typing import TypeVar

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

ItemT = TypeVar("ItemT")


class CursorsModel(BaseModel):
    after: Optional[str] = None
    before: Optional[str] = None


class PagedResultWithCursorsModel[ItemT](BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    href: HttpUrl
    limit: int
    next_page: Optional[HttpUrl] = Field(alias="next")
    cursors: CursorsModel
    items: Sequence[ItemT]
