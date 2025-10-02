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
    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
    method_type: HTTPMethod = HTTPMethod.PUT
    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        uris: Optional[Sequence[Union[SpotifyEpisodeURI, SpotifyTrackURI]]] = None,
        range_start: int,
        insert_before: int,
        range_length: int = 1,
        snapshot_id: Optional[str] = None,
    ) -> UpdatePlaylistItemsRequest:
        params = UpdatePlaylistItemsRequestParams(
            playlist_id=playlist_id,
            uris=uris,
        )
        body = UpdatePlaylistItemsRequestBody(
            uris=uris,
            range_start=range_start,
            insert_before=insert_before,
            range_length=range_length,
            snapshot_id=snapshot_id,
        )
        endpoint = f"playlists/{playlist_id}/tracks"

        return cls(endpoint=endpoint, params=params, body=body)
