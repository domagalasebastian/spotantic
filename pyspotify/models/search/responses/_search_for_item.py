from typing import Optional

from pydantic import BaseModel

from pyspotify.models.spotify import ArtistModel
from pyspotify.models.spotify import PagedResultModel
from pyspotify.models.spotify import SimplifiedAlbumModel
from pyspotify.models.spotify import SimplifiedEpisodeModel
from pyspotify.models.spotify import SimplifiedPlaylistModel
from pyspotify.models.spotify import SimplifiedShowModel
from pyspotify.models.spotify import TrackModel


class SearchForItemResponse(BaseModel):
    tracks: Optional[PagedResultModel[TrackModel]] = None
    artists: Optional[PagedResultModel[ArtistModel]] = None
    albums: Optional[PagedResultModel[SimplifiedAlbumModel]] = None
    playlists: Optional[PagedResultModel[SimplifiedPlaylistModel]] = None
    shows: Optional[PagedResultModel[SimplifiedShowModel]] = None
    episodes: Optional[PagedResultModel[SimplifiedEpisodeModel]] = None
