from __future__ import annotations

from http import HTTPMethod
from typing import Optional
from typing import Set

from pydantic import BaseModel
from pydantic import model_validator

from pyspotify.custom_types import Scope
from pyspotify.models import RequestHeadersModel
from pyspotify.models import RequestModel


class CreatePlaylistRequestParams(BaseModel):
    user_id: str


class CreatePlaylistRequestBody(BaseModel):
    name: str
    public: Optional[bool] = None
    collaborative: Optional[bool] = None
    description: Optional[str] = None

    @model_validator(mode="after")
    def validate_flags(self) -> CreatePlaylistRequestBody:
        if self.public is False and self.collaborative is True:
            raise ValueError("To create a collaborative playlist you must also set `public` to False!")

        return self


class CreatePlaylistRequest(RequestModel[CreatePlaylistRequestParams, CreatePlaylistRequestBody]):
    required_scopes: Set[Scope] = {Scope.PLAYLIST_MODIFY_PRIVATE, Scope.PLAYLIST_MODIFY_PUBLIC}
    method_type: HTTPMethod = HTTPMethod.POST
    headers: RequestHeadersModel = RequestHeadersModel(content_type="application/json")

    @classmethod
    def build(
        cls,
        *,
        user_id: str,
        name: str,
        description: Optional[str] = None,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
    ) -> CreatePlaylistRequest:
        params = CreatePlaylistRequestParams(user_id=user_id)
        body = CreatePlaylistRequestBody(
            name=name,
            public=public,
            collaborative=collaborative,
            description=description,
        )
        endpoint = f"users/{user_id}/playlists"

        return cls(endpoint=endpoint, params=params, body=body)
