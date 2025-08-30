from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.custom_types import SpotifyShowURI
from pyspotify.models.spotify._copyright_model import CopyrightModel
from pyspotify.models.spotify._image_model import ImageModel


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class SimplifiedShowModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    available_markets: Sequence[SpotifyMarketID] = Field(repr=False)
    copyrights: Sequence[CopyrightModel] = Field(repr=False)
    description: str
    html_description: str = Field(repr=False)
    explicit: bool
    external_urls: ExternalUrlsModel = Field(repr=False)
    show_href: HttpUrl = Field(alias="href")
    show_id: SpotifyItemID = Field(alias="id", repr=False)
    images: Sequence[ImageModel] = Field(repr=False)
    is_externally_hosted: bool = Field(repr=False)
    languages: Sequence[str]
    media_type: str
    show_name: str = Field(alias="name")
    publisher: str = Field(repr=False)
    item_type: Literal["show"] = Field(alias="type", repr=False)
    show_uri: SpotifyShowURI = Field(alias="uri", repr=False)
    total_episodes: int
