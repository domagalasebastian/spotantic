from typing import Annotated
from typing import Any
from typing import Optional

from pydantic import StringConstraints
from pydantic.types import Json

from ._spotify_types import AlbumTypes
from ._spotify_types import AuthScope
from ._spotify_types import RepeatMode
from ._spotify_types import SpotifyItemType

type APIResponse = Optional[Json[Any]]
"""API response type. JSON or `None`."""

type SpotifyMarketID = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        to_upper=True,
        pattern=r"^[A-Za-z]{2}$",
    ),
]
"""An ISO 3166-1 alpha-2 country code."""

type SpotifyLocaleID = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[A-Za-z]{2}_[A-Za-z]{2}$"),
]
"""An ISO 639-1 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore."""

type SpotifyItemID = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^[A-Za-z0-9]{22}$",
    ),
]
"""The base-62 identifier found at the end of the `SpotifyItemURI`."""

type SpotifyItemURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{'|'.join(item.value for item in SpotifyItemType)}:[A-Za-z0-9]{{22}}$",
    ),
]
"""The resource identifier of an item."""

type SpotifyAlbumURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ALBUM.value}:[A-Za-z0-9]{{22}}$",
    ),
]
"""The resource identifier of an album."""

type SpotifyArtistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ARTIST.value}:[A-Za-z0-9]{{22}}$",
    ),
]
"""The resource identifier of an artist."""

type SpotifyEpisodeURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.EPISODE.value}:[A-Za-z0-9]{{22}}$",
    ),
]
"""The resource identifier of an episode."""

type SpotifyPlaylistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.PLAYLIST.value}:[A-Za-z0-9]{{22}}$",
    ),
]
"""The resource identifier of a playlist."""

type SpotifyShowURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.SHOW.value}:[A-Za-z0-9]{{22}}$",
    ),
]
"""The resource identifier of a show."""

type SpotifyTrackURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.TRACK.value}:[A-Za-z0-9]{{22}}$",
    ),
]

type SpotifyUserURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.USER.value}:[A-Za-z0-9]*$",
    ),
]
"""The resource identifier of an user."""


__all__ = [
    "APIResponse",
    "AlbumTypes",
    "AuthScope",
    "RepeatMode",
    "SpotifyAlbumURI",
    "SpotifyArtistURI",
    "SpotifyEpisodeURI",
    "SpotifyItemID",
    "SpotifyItemType",
    "SpotifyItemURI",
    "SpotifyLocaleID",
    "SpotifyMarketID",
    "SpotifyPlaylistURI",
    "SpotifyShowURI",
    "SpotifyTrackURI",
    "SpotifyUserURI",
]
