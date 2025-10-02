from __future__ import annotations

from http import HTTPMethod
from typing import Optional
from typing import Set

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestHeadersModel
from pyspotify.models import RequestModel


class ChangePlaylistDetailsRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")


class ChangePlaylistDetailsRequestBody(BaseModel):
    name: Optional[str] = None
    public: Optional[bool] = None
    collaborative: Optional[bool] = None
    description: Optional[str] = None


class ChangePlaylistDetailsRequest(RequestModel[ChangePlaylistDetailsRequestParams, ChangePlaylistDetailsRequestBody]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
    method_type: HTTPMethod = HTTPMethod.PUT
    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        name: Optional[str] = None,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> ChangePlaylistDetailsRequest:
        params = ChangePlaylistDetailsRequestParams(playlist_id=playlist_id)
        body = ChangePlaylistDetailsRequestBody(
            name=name,
            public=public,
            collaborative=collaborative,
            description=description,
        )
        endpoint = f"playlists/{playlist_id}"

        return cls(endpoint=endpoint, params=params, body=body)
