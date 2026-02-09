from datetime import datetime
from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import AlbumTypes
from pyspotify.custom_types import SpotifyAlbumURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID

from ._image_model import ImageModel
from ._simplified_artist_model import SimplifiedArtistModel
from .submodels import ExternalUrlsModel
from .submodels import RestrictionsModel


class SimplifiedAlbumModel(BaseModel):
    """Model representing simplified Spotify catalog information for a single album."""

    model_config = ConfigDict(serialize_by_alias=True)

    album_type: AlbumTypes
    """The type of the album."""

    total_tracks: int
    """The number of tracks in the album."""

    available_markets: Sequence[SpotifyMarketID] = Field(repr=False)
    """The markets in which the album is available."""

    external_urls: ExternalUrlsModel = Field(repr=False)
    """Known external URLs for this album."""

    album_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the album."""

    album_id: SpotifyItemID = Field(alias="id", repr=False)
    """The Spotify ID for the album."""

    images: Sequence[ImageModel] = Field(repr=False)
    """The cover art for the album in various sizes, widest first."""

    album_name: str = Field(alias="name")
    """The name of the album. In case of an album takedown, the value may be an empty string."""

    release_date: datetime
    """The date the album was first released."""

    release_date_precision: Literal["year", "month", "day"] = Field(repr=False)
    """The precision with which release_date value is known."""

    restrictions: Optional[RestrictionsModel] = Field(None, repr=False)
    """Included in the response when a content restriction is applied."""

    item_type: Literal["album"] = Field(alias="type", repr=False)
    """The item type."""

    album_uri: SpotifyAlbumURI = Field(alias="uri", repr=False)
    """The Spotify URI for the album."""

    artists: Sequence[SimplifiedArtistModel]
    """The artists of the album."""
