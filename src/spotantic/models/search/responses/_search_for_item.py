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
    """Response model for Search For Item endpoint."""

    tracks: Optional[PagedResultModel[TrackModel]] = None
    """List of tracks."""

    artists: Optional[PagedResultModel[ArtistModel]] = None
    """List of atrists."""

    albums: Optional[PagedResultModel[SimplifiedAlbumModel]] = None
    """List of albums."""

    playlists: Optional[PagedResultModel[SimplifiedPlaylistModel]] = None
    """List of playlists."""

    shows: Optional[PagedResultModel[SimplifiedShowModel]] = None
    """List of shows."""

    episodes: Optional[PagedResultModel[SimplifiedEpisodeModel]] = None
    """List of episodes."""
