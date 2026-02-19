from ._paged_result_model import PagedResultModel
from ._playlist_base_model import PlaylistBaseModel
from ._playlist_track_model import PlaylistTrackModel


class PlaylistModel(PlaylistBaseModel):
    """Model representing a playlist owned by a Spotify user."""

    items: PagedResultModel[PlaylistTrackModel]
    """The tracks of the playlist."""
