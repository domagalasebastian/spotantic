from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import PlainSerializer

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import RequestHeadersModel
from pyspotify.models import RequestModel


class AddItemsToPlaylistRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    position: Optional[int] = None
    uris: Annotated[
        Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]],
        Field(max_length=100),
        PlainSerializer(lambda seq: ",".join(seq), return_type=str),
    ] = None


class AddItemsToPlaylistRequestBody(BaseModel):
    uris: Annotated[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]], Field(max_length=100)]
    position: Optional[int] = None


class AddItemsToPlaylistRequest(RequestModel[AddItemsToPlaylistRequestParams, AddItemsToPlaylistRequestBody]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
    method_type: HTTPMethod = HTTPMethod.POST
    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
        position: Optional[int] = None,
    ) -> AddItemsToPlaylistRequest:
        params = AddItemsToPlaylistRequestParams(playlist_id=playlist_id)
        body = AddItemsToPlaylistRequestBody(uris=uris, position=position)
        endpoint = f"playlists/{playlist_id}/tracks"

        return cls(endpoint=endpoint, params=params, body=body)
