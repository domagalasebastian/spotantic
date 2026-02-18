from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from spotantic.types import SpotifyArtistURI
from spotantic.types import SpotifyItemID

from .submodels import ExternalUrlsModel


class SimplifiedArtistModel(BaseModel):
    """Model representing simplified Spotify catalog information for a single artist."""

    model_config = ConfigDict(serialize_by_alias=True)

    external_urls: ExternalUrlsModel = Field(repr=False)
    """Known external URLs for this artist."""

    artist_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the artist."""

    artist_id: SpotifyItemID = Field(alias="id", repr=False)
    """The Spotify ID for the artist."""

    artist_name: str = Field(alias="name")
    """The name of the artist."""

    item_type: Literal["artist"] = Field(alias="type", repr=False)
    """The object type."""

    artist_uri: SpotifyArtistURI = Field(alias="uri", repr=False)
    """The Spotify URI for the artist."""
