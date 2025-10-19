from typing import Any
from typing import Optional

from pydantic.types import Json

from ._auth_scope import Scope
from ._generic_custom_types import ParamsBool
from ._spotify_api_types import AlbumTypes
from ._spotify_api_types import RepeatMode
from ._spotify_api_types import SpotifyAlbumURI
from ._spotify_api_types import SpotifyArtistURI
from ._spotify_api_types import SpotifyEpisodeURI
from ._spotify_api_types import SpotifyItemID
from ._spotify_api_types import SpotifyItemType
from ._spotify_api_types import SpotifyItemURI
from ._spotify_api_types import SpotifyLocaleID
from ._spotify_api_types import SpotifyMarketID
from ._spotify_api_types import SpotifyPlaylistURI
from ._spotify_api_types import SpotifyShowURI
from ._spotify_api_types import SpotifyTrackURI
from ._spotify_api_types import SpotifyUserURI

type APIResponse = Optional[Json[Any]]

__all__ = [
    "APIResponse",
    "AlbumTypes",
    "ParamsBool",
    "RepeatMode",
    "Scope",
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
