from pyspotify.models.spotify._paged_result_model import PagedResultModel
from pyspotify.models.spotify._simplified_episode_model import SimplifiedEpisodeModel
from pyspotify.models.spotify._simplified_show_model import SimplifiedShowModel


class ShowModel(SimplifiedShowModel):
    episodes: PagedResultModel[SimplifiedEpisodeModel]
