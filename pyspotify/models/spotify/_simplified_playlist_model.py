from typing import Optional

from ._playlist_base_model import PlaylistBaseModel
from ._playlist_summary_model import PlaylistSummaryModel


class SimplifiedPlaylistModel(PlaylistBaseModel):
    """Model representing simplified Spotify catalog information for a single playlist."""

    tracks: Optional[PlaylistSummaryModel] = None
    """A collection containing a link ( href ) to the Web API endpoint where
    full details of the playlist's tracks can be retrieved."""
