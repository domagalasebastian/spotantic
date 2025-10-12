from __future__ import annotations

from enum import Enum
from typing import Annotated

from pydantic import StringConstraints


class SpotifyItemType(str, Enum):
    ALBUM = "album"
    ARTIST = "artist"
    EPISODE = "episode"
    PLAYLIST = "playlist"
    SHOW = "show"
    TRACK = "track"
    USER = "user"


class AlbumTypes(str, Enum):
    ALBUM = "album"
    SINGLE = "single"
    APPEARS_ON = "appears_on"
    COMPILATION = "compilation"


class RepeatMode(str, Enum):
    TRACK = "track"
    CONTEXT = "context"
    OFF = "off"


type SpotifyMarketID = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        to_upper=True,
        pattern=r"^[A-Za-z]{2}$",
    ),
]

type SpotifyLocaleID = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[A-Za-z]{2}_[A-Za-z]{2}$"),
]

type SpotifyItemID = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^[A-Za-z0-9]{22}$",
    ),
]

type SpotifyItemURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{'|'.join(item.value for item in SpotifyItemType)}:[A-Za-z0-9]{{22}}$",
    ),
]

type SpotifyAlbumURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ALBUM.value}:[A-Za-z0-9]{{22}}$",
    ),
]

type SpotifyArtistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ARTIST.value}:[A-Za-z0-9]{{22}}$",
    ),
]

type SpotifyEpisodeURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.EPISODE.value}:[A-Za-z0-9]{{22}}$",
    ),
]

type SpotifyPlaylistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.PLAYLIST.value}:[A-Za-z0-9]{{22}}$",
    ),
]

type SpotifyShowURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.SHOW.value}:[A-Za-z0-9]{{22}}$",
    ),
]

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
