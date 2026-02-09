from ._paged_result_model import PagedResultModel
from ._simplified_episode_model import SimplifiedEpisodeModel
from ._simplified_show_model import SimplifiedShowModel


class ShowModel(SimplifiedShowModel):
    """Model representing catalog information for a single show identified by its unique Spotify ID."""

    episodes: PagedResultModel[SimplifiedEpisodeModel]
    """The episodes of the show."""
