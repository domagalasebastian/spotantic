from typing import TypeAliasType

import pytest

from spotantic.types import SpotifyAlbumURI
from spotantic.types import SpotifyArtistURI
from spotantic.types import SpotifyEpisodeURI
from spotantic.types import SpotifyItemID
from spotantic.types import SpotifyLocaleID
from spotantic.types import SpotifyMarketID
from spotantic.types import SpotifyPlaylistURI
from spotantic.types import SpotifyShowURI
from spotantic.types import SpotifyTrackURI
from spotantic.types import SpotifyUserURI

_example_instances_of_type = {
    SpotifyAlbumURI: "spotify:album:AaBbCcDdEeFfGgHhIiJjKk",
    SpotifyArtistURI: "spotify:artist:AaBbCcDdEeFfGgHhIiJjKk",
    SpotifyEpisodeURI: "spotify:episode:AaBbCcDdEeFfGgHhIiJjKk",
    SpotifyItemID: "AaBbCcDdEeFfGgHhIiJjKk",
    SpotifyLocaleID: "en_EN",
    SpotifyMarketID: "EN",
    SpotifyPlaylistURI: "spotify:playlist:AaBbCcDdEeFfGgHhIiJjKk",
    SpotifyShowURI: "spotify:show:AaBbCcDdEeFfGgHhIiJjKk",
    SpotifyTrackURI: "spotify:track:AaBbCcDdEeFfGgHhIiJjKk",
    SpotifyUserURI: "spotify:user:AaBbCcDdEeFfGgHhIiJjKk",
}


@pytest.fixture
def example_instances_of_type() -> dict[TypeAliasType, str]:
    return _example_instances_of_type
