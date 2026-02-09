from ._simplified_episode_model import SimplifiedEpisodeModel
from ._simplified_show_model import SimplifiedShowModel


class EpisodeModel(SimplifiedEpisodeModel):
    """Model representing catalog information for a single episode identified by its unique Spotify ID."""

    show: SimplifiedShowModel
    """The show on which the episode belongs."""
