from collections.abc import Sequence
from typing import Optional

from pydantic import Field

from ._image_model import ImageModel
from ._simplified_artist_model import SimplifiedArtistModel
from .submodels import ArtistFollowersModel


class ArtistModel(SimplifiedArtistModel):
    """Model representing Spotify catalog information for a single artist identified by their unique Spotify ID."""

    followers: Optional[ArtistFollowersModel] = Field(None, repr=False, deprecated=True)
    """Information about the followers of the artist."""

    genres: Sequence[str]
    """A list of the genres the artist is associated with. If not yet classified, the array is empty."""

    images: Sequence[ImageModel] = Field(repr=False)
    """Images of the artist in various sizes, widest first."""

    popularity: Optional[int] = Field(None, repr=False, deprecated=True)
    """The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular.
    The artist's popularity is calculated from the popularity of all the artist's tracks."""
