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


SpotifyMarketID = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        to_upper=True,
        pattern=r"^[A-Za-z]{2}$",
    ),
]

SpotifyItemID = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=r"^[A-Za-z0-9]{22}$",
    ),
]

SpotifyItemURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{"|".join(item for item in SpotifyItemType)}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyAlbumURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ALBUM}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyArtistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ARTIST}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyEpisodeURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.EPISODE}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyPlaylistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.PLAYLIST}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyShowURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.SHOW}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyTrackURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.TRACK}:[A-Za-z0-9]{{22}}$",
    ),
]
