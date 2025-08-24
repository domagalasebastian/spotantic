from __future__ import annotations

from enum import Enum
from typing import Annotated
from typing import Tuple

from pydantic import AfterValidator
from pydantic import StringConstraints


class SpotifyItemType(str, Enum):
    ALBUM = "album"
    ARTIST = "artist"
    EPISODE = "episode"
    PLAYLIST = "playlist"
    SHOW = "show"
    TRACK = "track"

    @classmethod
    def playback_supported_item_types(cls) -> Tuple[SpotifyItemType, ...]:
        return (cls.EPISODE, cls.TRACK)

    @classmethod
    def check_value_is_playback_supported(cls, value: SpotifyItemType) -> SpotifyItemType:
        if value not in cls.playback_supported_item_types():
            raise ValueError(f"{value} is not valid item type supported by playback!")

        return value


class AlbumTypes(str, Enum):
    ALBUM = "album"
    SINGLE = "single"
    APPEARS_ON = "appears_on"
    COMPILATION = "compilation"


class RepeatMode(str, Enum):
    TRACK = "track"
    CONTEXT = "context"
    OFF = "off"


PlaybackSupportedItemType = Annotated[
    SpotifyItemType,
    AfterValidator(SpotifyItemType.check_value_is_playback_supported),
]

SpotifyMarketID = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        to_upper=True,
        pattern=r"^[A-Za-z]{2}$",
    ),
]

SpotifyLocaleID = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[A-Za-z]{2}_[A-Za-z]{2}$"),
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
        pattern=rf"^spotify:{"|".join(item.value for item in SpotifyItemType)}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyAlbumURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ALBUM.value}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyArtistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.ARTIST.value}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyEpisodeURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.EPISODE.value}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyPlaylistURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.PLAYLIST.value}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyShowURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.SHOW.value}:[A-Za-z0-9]{{22}}$",
    ),
]

SpotifyTrackURI = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        pattern=rf"^spotify:{SpotifyItemType.TRACK.value}:[A-Za-z0-9]{{22}}$",
    ),
]
