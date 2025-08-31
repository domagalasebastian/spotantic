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

from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class TimestampTrackIDModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    track_id: SpotifyItemID = Field(serialization_alias="id")
    added_at: Annotated[
        datetime,
        PlainSerializer(lambda date: date.astimezone(timezone.utc).isoformat(), return_type=str),
    ]


class SaveTracksForCurrentUserRequestBody(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    track_ids: Annotated[
        Optional[Sequence[SpotifyItemID]],
        Field(None, max_length=50, serialization_alias="ids"),
    ]
    timestamped_ids: Optional[Sequence[TimestampTrackIDModel]] = None


class SaveTracksForCurrentUserRequest(RequestModel[None, SaveTracksForCurrentUserRequestBody]):
    method_type: HTTPMethod = HTTPMethod.PUT
