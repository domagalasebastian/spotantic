from __future__ import annotations

from datetime import datetime
from datetime import timezone
from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer
from pydantic import model_validator

from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


class TimestampTrackIDModel(BaseModel):
    """Model for track ID with timestamp."""

    model_config = ConfigDict(serialize_by_alias=True)

    track_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID for the track."""

    added_at: Annotated[
        datetime,
        PlainSerializer(lambda date: date.astimezone(timezone.utc).isoformat(), return_type=str),
    ]
    """The timestamp when the track was added."""


class SaveTracksForCurrentUserRequestBody(BaseModel):
    """Body model for Save Tracks For Current User request."""

    model_config = ConfigDict(serialize_by_alias=True)

    track_ids: Annotated[
        Optional[Sequence[SpotifyItemID]],
        Field(None, max_length=50, serialization_alias="ids"),
    ]
    """A list of the Spotify IDs for the tracks."""

    timestamped_ids: Optional[Sequence[TimestampTrackIDModel]] = None
    """A list of track IDs with timestamps."""

    @model_validator(mode="after")
    def check_either_field(self) -> SaveTracksForCurrentUserRequestBody:
        """Validates that either track_ids or timestamped_ids is provided.

        Args:
            model: The model instance to validate.

        Returns:
            The validated model instance.

        Raises:
            ValueError: If neither of the fields is provided.
        """
        if self.track_ids is None and self.timestamped_ids is None:
            raise ValueError("Either 'track_ids' or 'timestamped_ids' must be provided.")

        return self


class SaveTracksForCurrentUserRequest(RequestModel[None, SaveTracksForCurrentUserRequestBody]):
    """Request model for Save Tracks For Current User endpoint."""

    required_scopes: set[AuthScope] = {AuthScope.USER_LIBRARY_MODIFY}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/tracks"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        track_ids: Optional[Sequence[SpotifyItemID]] = None,
        timestamped_ids: Optional[dict[SpotifyItemID, datetime]] = None,
    ) -> SaveTracksForCurrentUserRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            track_ids: A list of the Spotify IDs for the tracks.
            timestamped_ids: A dictionary mapping Spotify track IDs to their added timestamps.

        Returns:
            Validated Request object.
        """
        timestamped_models = None
        if timestamped_ids is not None:
            timestamped_models = [
                TimestampTrackIDModel(track_id=track_id, added_at=added_at)
                for track_id, added_at in timestamped_ids.items()
            ]

        body = SaveTracksForCurrentUserRequestBody(
            track_ids=track_ids,
            timestamped_ids=timestamped_models,
        )

        return cls(body=body)
