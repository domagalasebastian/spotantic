from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class CopyrightModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    text: str
    copyright_type: Literal["C", "P"] = Field(alias="type", repr=False)
