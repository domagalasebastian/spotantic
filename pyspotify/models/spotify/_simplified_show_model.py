from typing import Literal
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.custom_types import SpotifyShowURI

from ._image_model import ImageModel
from .submodels import CopyrightModel
from .submodels import ExternalUrlsModel


class SimplifiedShowModel(BaseModel):
    """Model representing simplified Spotify catalog information for a single show."""

    model_config = ConfigDict(serialize_by_alias=True)

    available_markets: Sequence[SpotifyMarketID] = Field(repr=False)
    """A list of the countries in which the show can be played, identified by their ISO 3166-1 alpha-2 code."""

    copyrights: Sequence[CopyrightModel] = Field(repr=False)
    """The copyright statements of the show."""

    description: str
    """A description of the show. HTML tags are stripped away from this field."""

    html_description: str = Field(repr=False)
    """A description of the show. This field may contain HTML tags."""

    explicit: bool
    """Whether or not the show has explicit content."""

    external_urls: ExternalUrlsModel = Field(repr=False)
    """External URLs for this show."""

    show_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the show."""

    show_id: SpotifyItemID = Field(alias="id", repr=False)
    """The Spotify ID for the show."""

    images: Sequence[ImageModel] = Field(repr=False)
    """The cover art for the show in various sizes, widest first."""

    is_externally_hosted: bool = Field(repr=False)
    """`True` if all of the shows episodes are hosted outside of Spotify's CDN."""

    languages: Sequence[str]
    """A list of the languages used in the show, identified by their ISO 639 code."""

    media_type: str
    """The media type of the show."""

    show_name: str = Field(alias="name")
    """The name of the episode."""

    publisher: str = Field(repr=False)
    """The publisher of the show."""

    item_type: Literal["show"] = Field(alias="type", repr=False)
    """The item type."""

    show_uri: SpotifyShowURI = Field(alias="uri", repr=False)
    """The Spotify URI for the show."""

    total_episodes: int
    """The total number of episodes in the show."""
