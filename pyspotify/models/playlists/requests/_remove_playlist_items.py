from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import RequestModel


class RemovePlaylistItemsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")


class RemovePlaylistItemsRequestBody(BaseModel):
    tracks: Annotated[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]], Field(max_length=100)]
    snapshot_id: Optional[str] = None


class RemovePlaylistItemsRequest(RequestModel[RemovePlaylistItemsRequestParams, RemovePlaylistItemsRequestBody]):
    method_type: HTTPMethod = HTTPMethod.DELETE
