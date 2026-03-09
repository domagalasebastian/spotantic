from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl


class PlaylistSummaryModel(BaseModel):
    """Model representing information to retrieve full details of the playlist's tracks."""

    model_config = ConfigDict(serialize_by_alias=True)

    tracks_href: HttpUrl = Field(alias="href")
    """A link to the Web API endpoint where full details of the playlist's tracks can be retrieved."""

    tracks_total: int = Field(alias="total")
    """Number of tracks in the playlist."""
