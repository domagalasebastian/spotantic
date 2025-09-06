from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer
from pydantic import field_validator

from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetPlaylistRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)
    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    fields: Optional[str] = None
    additional_types: Annotated[Sequence[SpotifyItemType], PlainSerializer(lambda seq: ",".join(seq), return_type=str)]
    market: Optional[SpotifyMarketID] = None

    @field_validator("additional_types", mode="after")
    def check_value_is_playback_supported(cls, value: Sequence[SpotifyItemType]) -> Sequence[SpotifyItemType]:
        if any(item not in (SpotifyItemType.TRACK, SpotifyItemType.EPISODE) for item in value):
            raise ValueError(f"{value} is not valid item type supported by playback!")

        return value


class GetPlaylistRequest(RequestModel[GetPlaylistRequestParams, None]):
    method_type: HTTPMethod = HTTPMethod.GET
