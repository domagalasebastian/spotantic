from typing import Literal
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl

from pyspotify.types import SpotifyItemID
from pyspotify.types import SpotifyPlaylistURI

from ._image_model import ImageModel
from .submodels import ExternalUrlsModel
from .submodels import PlaylistOwnerModel


class PlaylistBaseModel(BaseModel):
    """Model containing common fields for playlist objects."""

    model_config = ConfigDict(serialize_by_alias=True)

    collaborative: bool = Field(repr=False)
    """`True` if the owner allows other users to modify the playlist."""

    description: Optional[str] = None
    """The playlist description."""

    external_urls: ExternalUrlsModel = Field(repr=False)
    """Known external URLs for this playlist."""

    playlist_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint providing full details of the playlist."""

    playlist_id: SpotifyItemID = Field(alias="id", repr=False)
    """The Spotify ID for the playlist."""

    images: Sequence[ImageModel] = Field(repr=False)
    """Images for the playlist. The array may be empty or contain up to three images.
    The images are returned by size in descending order."""

    playlist_name: str = Field(alias="name")
    """The name of the playlist."""

    owner: PlaylistOwnerModel
    """The user who owns the playlist"""

    public: Optional[bool] = Field(None, repr=False)
    """`True` the playlist is public, `False` the playlist is private, `None` the playlist status is not relevant."""

    snapshot_id: str
    """The version identifier for the current playlist. Can be supplied in other requests to target a specific playlist version."""

    item_type: Literal["playlist"] = Field(alias="type", repr=False)
    """The item type."""

    playlist_uri: SpotifyPlaylistURI = Field(alias="uri", repr=False)
    """The Spotify URI for the playlist."""
