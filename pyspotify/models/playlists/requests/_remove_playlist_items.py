from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic.functional_serializers import PlainSerializer

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyEpisodeURI
from pyspotify.custom_types import SpotifyItemID
from pyspotify.custom_types import SpotifyTrackURI
from pyspotify.models import RequestHeadersModel
from pyspotify.models import RequestModel


class RemovePlaylistItemsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")


class RemovePlaylistItemsRequestBody(BaseModel):
    tracks: Annotated[
        Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
        Field(max_length=100),
        PlainSerializer(lambda seq: [{"uri": uri} for uri in seq], return_type=List[Dict[str, str]]),
    ]
    snapshot_id: Optional[str] = None


class RemovePlaylistItemsRequest(RequestModel[RemovePlaylistItemsRequestParams, RemovePlaylistItemsRequestBody]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
    method_type: HTTPMethod = HTTPMethod.DELETE
    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        uris: Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]],
        snapshot_id: Optional[str] = None,
    ) -> RemovePlaylistItemsRequest:
        params = RemovePlaylistItemsRequestParams(playlist_id=playlist_id)
        body = RemovePlaylistItemsRequestBody(
            tracks=uris,
            snapshot_id=snapshot_id,
        )
        endpoint = f"playlists/{playlist_id}/tracks"

        return cls(endpoint=endpoint, params=params, body=body)
