from pydantic import BaseModel

from spotantic.models.spotify import EpisodeModel


class GetSeveralEpisodesResponse(BaseModel):
    """Response model for Get Several Episodes endpoint."""

    episodes: list[EpisodeModel]
    """List of episodes."""
