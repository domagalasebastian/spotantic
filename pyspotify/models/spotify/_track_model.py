from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.models.spotify._simplified_album_model import SimplifiedAlbumModel
from pyspotify.models.spotify._simplified_track_model import SimplifiedTrackModel


class ExternalIdsModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    international_standard_recording_code: Optional[str] = Field(None, alias="isrc")
    international_article_number: Optional[str] = Field(None, alias="ean")
    universal_product_code: Optional[str] = Field(None, alias="upc")


class TrackModel(SimplifiedTrackModel):
    album: SimplifiedAlbumModel
    external_ids: ExternalIdsModel = Field(repr=False)
    popularity: int
