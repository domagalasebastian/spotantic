from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.types import SpotifyItemType
from pyspotify.types import SpotifyItemURI

from ._external_urls_model import ExternalUrlsModel


class ContextModel(BaseModel):
    """Model representing information about playback context."""

    model_config = ConfigDict(serialize_by_alias=True)

    context_type: SpotifyItemType = Field(alias="type")
    """The item type."""

    context_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the item."""

    external_urls: ExternalUrlsModel = Field(repr=False)
    """External URLs for this context."""

    context_uri: SpotifyItemURI = Field(alias="uri", repr=False)
    """The Spotify URI for the context."""
