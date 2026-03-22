from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl


class ImageModel(BaseModel):
    """Model representing an image data."""

    model_config = ConfigDict(serialize_by_alias=True)

    image_url: HttpUrl = Field(alias="url")
    """The source URL of the image."""

    height: Optional[int] = None
    """The image height in pixels."""

    width: Optional[int] = None
    """The image width in pixels."""
