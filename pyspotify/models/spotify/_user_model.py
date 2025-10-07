from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyMarketID
from pyspotify.custom_types import SpotifyUserURI
from pyspotify.models.spotify._image_model import ImageModel


class ExplicitContentModel(BaseModel):
    filter_enabled: bool
    filter_locked: bool


class ExternalUrlsModel(BaseModel):
    spotify: Optional[HttpUrl] = None


class FollowersModel(BaseModel):
    followers_href: Optional[HttpUrl] = Field(None, repr=False)
    total: int


class UserModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    display_name: Optional[str] = None
    external_urls: ExternalUrlsModel = Field(repr=False)
    user_href: HttpUrl = Field(alias="href")
    user_id: str = Field(alias="id")
    images: Sequence[ImageModel] = Field(repr=False)
    item_type: Literal["user"] = Field(alias="type", repr=False)
    user_uri: SpotifyUserURI = Field(alias="uri", repr=False)


class CurrentUserModel(UserModel):
    country: Optional[SpotifyMarketID] = None
    email: Optional[str] = None
    explicit_content: Optional[ExplicitContentModel] = Field(None, repr=False)
    followers: FollowersModel
    product: Optional[str] = None
