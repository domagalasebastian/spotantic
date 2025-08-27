from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.models.spotify._image_model import ImageModel


class CategoryModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    category_href: HttpUrl = Field(alias="href")
    icons: Sequence[ImageModel] = Field(repr=False)
    category_id: str = Field(alias="id")
    category_name: str = Field(alias="name")
