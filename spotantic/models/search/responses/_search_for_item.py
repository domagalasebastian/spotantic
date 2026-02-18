from typing import Optional

from pydantic import BaseModel

from spotantic.models.spotify import ArtistModel
from spotantic.models.spotify import PagedResultModel
from spotantic.models.spotify import SimplifiedAlbumModel
from spotantic.models.spotify import SimplifiedEpisodeModel
from spotantic.models.spotify import SimplifiedPlaylistModel
from spotantic.models.spotify import SimplifiedShowModel
from spotantic.models.spotify import TrackModel


class SearchForItemResponse(BaseModel):
    tracks: Optional[PagedResultModel[TrackModel]] = None
    artists: Optional[PagedResultModel[ArtistModel]] = None
    albums: Optional[PagedResultModel[SimplifiedAlbumModel]] = None
    playlists: Optional[PagedResultModel[SimplifiedPlaylistModel]] = None
    shows: Optional[PagedResultModel[SimplifiedShowModel]] = None
    episodes: Optional[PagedResultModel[SimplifiedEpisodeModel]] = None
