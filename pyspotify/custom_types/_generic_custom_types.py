from typing import Annotated
from typing import Sequence
from typing import TypeVar

from pydantic import Field

T = TypeVar("T")


BoundedInt1to50 = Annotated[int, Field(ge=1, le=50)]

SequenceMaxLen20 = Annotated[Sequence[T], Field(max_length=20)]
