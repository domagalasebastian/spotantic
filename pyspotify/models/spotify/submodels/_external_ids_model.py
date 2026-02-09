from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ExternalIdsModel(BaseModel):
    """Model representing known external IDs."""

    model_config = ConfigDict(serialize_by_alias=True)

    international_standard_recording_code: Optional[str] = Field(None, alias="isrc")
    """International Standard Recording Code."""

    international_article_number: Optional[str] = Field(None, alias="ean")
    """International Article Number."""

    universal_product_code: Optional[str] = Field(None, alias="upc")
    """Universal Product Code."""
