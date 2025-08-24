from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.models.spotify._copyright_model import CopyrightModel
from pyspotify.models.spotify._paged_result_model import PagedResultModel
from pyspotify.models.spotify._simplified_album_model import SimplifiedAlbumModel
from pyspotify.models.spotify._simplified_track_model import SimplifiedTrackModel


class ExternalIdsModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    international_standard_recording_code: Optional[str] = Field(None, alias="isrc")
    international_article_number: Optional[str] = Field(None, alias="ean")
    universal_product_code: Optional[str] = Field(None, alias="upc")


class AlbumModel(SimplifiedAlbumModel):
    tracks: PagedResultModel[SimplifiedTrackModel]
    copyrights: Sequence[CopyrightModel] = Field(repr=False)
    external_ids: ExternalIdsModel = Field(repr=False)
    genres: Sequence[str] = Field(repr=False, deprecated="Deprecated: The array is always empty.")
    label: str
    popularity: int
