from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import RequestModel


class UpdatePlaylistItemsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    uris: Annotated[
        Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]],
        Field(None, max_length=100),
        PlainSerializer(lambda seq: ",".join(seq), return_type=str),
    ]


class UpdatePlaylistItemsRequestBody(BaseModel):
    uris: Annotated[Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]], Field(None, max_length=100)]
    range_start: int
    insert_before: int
    range_length: Optional[int] = None
    snapshot_id: Optional[str] = None


class UpdatePlaylistItemsRequest(RequestModel[UpdatePlaylistItemsRequestParams, UpdatePlaylistItemsRequestBody]):
    method_type: HTTPMethod = HTTPMethod.PUT
