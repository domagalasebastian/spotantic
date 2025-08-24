from datetime import datetime
from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyAlbumURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models.spotify._image_model import ImageModel
from pyspotify.models.spotify._simplified_artist_model import SimplifiedArtistModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class RestrictionsModel(BaseModel):
    reason: Optional[Literal["market", "product", "explicit"]] = None


class ExternalIdsModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    international_standard_recording_code: Optional[str] = Field(None, alias="isrc")
    international_article_number: Optional[str] = Field(None, alias="ean")
    universal_product_code: Optional[str] = Field(None, alias="upc")


class SimplifiedAlbumModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    album_type: Literal["album", "single", "compilation"]
    total_tracks: int
    available_markets: Sequence[SpotifyMarketID] = Field(repr=False)
    external_urls: ExternalUrlsModel = Field(repr=False)
    album_href: HttpUrl = Field(alias="href")
    album_id: SpotifyItemID = Field(alias="id", repr=False)
    images: Sequence[ImageModel] = Field(repr=False)
    album_name: str = Field(alias="name")
    release_date: datetime
    release_date_precision: Literal["year", "month", "day"] = Field(repr=False)
    restrictions: Optional[RestrictionsModel] = Field(None, repr=False)
    item_type: Literal["album"] = Field(alias="type", repr=False)
    album_uri: SpotifyAlbumURI = Field(alias="uri", repr=False)
    artists: Sequence[SimplifiedArtistModel]
