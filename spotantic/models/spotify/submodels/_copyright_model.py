from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class CopyrightModel(BaseModel):
    """Model representing the copyright statements."""

    model_config = ConfigDict(serialize_by_alias=True)

    text: str
    """The copyright text for this content."""

    copyright_type: Literal["C", "P"] = Field(alias="type", repr=False)
    """The type of copyright."""
