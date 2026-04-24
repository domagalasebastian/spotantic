from collections.abc import Sequence
from datetime import date
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl
from pydantic import model_validator

from spotantic.types import AlbumTypes
from spotantic.types import SpotifyAlbumURI
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyMarketID

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

    available_markets: Optional[Sequence[SpotifyMarketID]] = Field(None, repr=False, deprecated=True)
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

    release_date: date
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

    album_group: Optional[str] = Field(None, repr=False, deprecated=True)
    """This field describes the relationship between the artist and the album."""

    @model_validator(mode="before")
    @classmethod
    def fix_date_by_precision(cls, data: dict) -> dict:
        """Fixes the `release_date` field based on the `release_date_precision` field.

        Args:
            data: The input data to validate.

        Returns:
            The validated data with fixed `release_date` field.
        """
        release_date = data.get("release_date")
        precision = data.get("release_date_precision")

        if precision == "year":
            data["release_date"] = f"{release_date}-01-01"
        elif precision == "month":
            data["release_date"] = f"{release_date}-01"

        return data
