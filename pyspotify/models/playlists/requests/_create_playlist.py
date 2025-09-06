from __future__ import annotations

from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import model_validator

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
    method_type: HTTPMethod = HTTPMethod.POST
