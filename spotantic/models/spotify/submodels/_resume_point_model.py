from datetime import timedelta

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator


class ResumePointModel(BaseModel):
    """Model representing user's most recent position in the episode."""

    model_config = ConfigDict(serialize_by_alias=True)

    fully_played: bool
    """Whether or not the episode has been fully played by the user."""

    resume_position: timedelta = Field(alias="resume_position_ms")
    """The user's most recent position in the episode in milliseconds."""

    @field_validator("resume_position", mode="before")
    def convert_resume_position_ms_to_timedelta(cls, value: int) -> timedelta:
        """Converts a resume position given in milliseconds to `timedelta` object.

        Args:
            value: Resume position [milliseconds].

        Returns:
            Resume position as `timedelta` object.
        """
        return timedelta(milliseconds=value)
