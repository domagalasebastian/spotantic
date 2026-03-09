from collections.abc import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from ._image_model import ImageModel


class CategoryModel(BaseModel):
    """Model representing a single category used to tag items in Spotify."""

    model_config = ConfigDict(serialize_by_alias=True)

    category_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint returning full details of the category."""

    icons: Sequence[ImageModel] = Field(repr=False)
    """The category icon, in various sizes."""

    category_id: str = Field(alias="id")
    """The Spotify category ID of the category."""

    category_name: str = Field(alias="name")
    """The name of the category."""
