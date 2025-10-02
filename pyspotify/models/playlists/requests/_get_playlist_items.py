from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Set

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer
from pydantic import field_validator

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyItemType
from pyspotify.custom_types import SpotifyMarketID
from pyspotify.models import RequestModel


class GetPlaylistItemsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)
    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    fields: Optional[str] = None
    limit: Annotated[int, Field(ge=1, le=50)]
    offset: int
    additional_types: Annotated[Sequence[SpotifyItemType], PlainSerializer(lambda seq: ",".join(seq), return_type=str)]
    market: Optional[SpotifyMarketID] = None

    @field_validator("additional_types", mode="after")
    def check_value_is_playback_supported(cls, value: Sequence[SpotifyItemType]) -> Sequence[SpotifyItemType]:
        if any(item not in (SpotifyItemType.TRACK, SpotifyItemType.EPISODE) for item in value):
            raise ValueError(f"{value} is not valid item type supported by playback!")

        return value


class GetPlaylistItemsRequest(RequestModel[GetPlaylistItemsRequestParams, None]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_READ_PRIVATE}
    method_type: HTTPMethod = HTTPMethod.GET

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        fields: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
        additional_types: Sequence[SpotifyItemType] = (SpotifyItemType.TRACK,),
        market: Optional[SpotifyMarketID] = None,
    ) -> GetPlaylistItemsRequest:
        params = GetPlaylistItemsRequestParams(
            playlist_id=playlist_id,
            fields=fields,
            limit=limit,
            offset=offset,
            additional_types=additional_types,
            market=market,
        )
        endpoint = f"playlists/{playlist_id}/tracks"

        return cls(endpoint=endpoint, params=params)
