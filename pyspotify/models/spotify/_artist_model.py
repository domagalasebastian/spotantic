from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.models.spotify._image_model import ImageModel
from pyspotify.models.spotify._simplified_artist_model import SimplifiedArtistModel


class FollowersModel(BaseModel):
    href: Optional[HttpUrl] = None
    total: int


class ArtistModel(SimplifiedArtistModel):
    followers: FollowersModel
    genres: Sequence[str]
    images: Sequence[ImageModel] = Field(repr=False)
    popularity: int
