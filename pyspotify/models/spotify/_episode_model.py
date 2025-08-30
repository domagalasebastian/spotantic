from pyspotify.models.spotify._simplified_episode_model import SimplifiedEpisodeModel
from pyspotify.models.spotify._simplified_show_model import SimplifiedShowModel


class EpisodeModel(SimplifiedEpisodeModel):
    show: SimplifiedShowModel
