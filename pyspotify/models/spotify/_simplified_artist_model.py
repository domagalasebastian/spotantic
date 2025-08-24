from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyArtistURI
from pyspotify.custom_types import SpotifyItemID


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class SimplifiedArtistModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    external_urls: ExternalUrlsModel = Field(repr=False)
    artist_href: HttpUrl = Field(alias="href")
    artist_id: SpotifyItemID = Field(alias="id", repr=False)
    artist_name: str = Field(alias="name")
    item_type: Literal["artist"] = Field(alias="type", repr=False)
    artist_uri: SpotifyArtistURI = Field(alias="uri", repr=False)
