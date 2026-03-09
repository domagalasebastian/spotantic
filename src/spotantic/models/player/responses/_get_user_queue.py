from typing import Annotated
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field

from spotantic.models.spotify import EpisodeModel
from spotantic.models.spotify import TrackModel


class GetUserQueueResponse(BaseModel):
    """Response model for Get User Queue endpoint."""

    currently_playing: Optional[Union[TrackModel, EpisodeModel]] = Field(None, discriminator="item_type")
    """The currently playing track or episode."""

    queue: list[Annotated[Union[TrackModel, EpisodeModel], Field(discriminator="item_type")]]
    """The tracks or episodes in the queue."""
