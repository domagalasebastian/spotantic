from typing import Annotated
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field

from pyspotify.models.spotify._episode_model import EpisodeModel
from pyspotify.models.spotify._track_model import TrackModel


# TODO: Move to player/responses package if there will not be any more usages
class UserQueueModel(BaseModel):
    currently_playing: Optional[Union[TrackModel, EpisodeModel]] = Field(discriminator="item_type")
    queue: List[Annotated[Union[TrackModel, EpisodeModel], Field(discriminator="item_type")]]
