from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl


class ImageModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    image_url: HttpUrl = Field(alias="url")
    height: Optional[int]
    width: Optional[int]
