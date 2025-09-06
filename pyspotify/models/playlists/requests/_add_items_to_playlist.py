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


class AddItemsToPlaylistRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    position: Optional[int] = None
    uris: Annotated[
        Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
        Field(max_length=100),
        PlainSerializer(lambda seq: ",".join(seq), return_type=str),
    ]


class AddItemsToPlaylistRequestBody(BaseModel):
    uris: Annotated[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]], Field(max_length=100)]
    position: Optional[int] = None


class AddItemsToPlaylistRequest(RequestModel[AddItemsToPlaylistRequestParams, AddItemsToPlaylistRequestBody]):
    method_type: HTTPMethod = HTTPMethod.POST
