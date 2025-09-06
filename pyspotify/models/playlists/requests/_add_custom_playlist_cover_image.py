from __future__ import annotations

import base64
from http import HTTPMethod
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import FilePath
from pydantic import model_serializer
from pydantic import model_validator

from pyspotify.custom_types import SpotifyItemID
from pyspotify.models import RequestModel


class AddCustomPlaylistCoverImageRequestParams(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)
    playlist_id: SpotifyItemID = Field(serialization_alias="id")


class AddCustomPlaylistCoverImageRequestBody(BaseModel):
    image_data: Optional[bytes] = None
    file_path: Optional[FilePath] = None

    @model_validator(mode="after")
    def get_image_data_from_file(self) -> AddCustomPlaylistCoverImageRequestBody:
        if self.image_data is not None:
            return self

        if self.file_path is None:
            raise ValueError("Either `image_data` or `file_path` must be provided!")

        if self.file_path.suffix not in (".jpeg", ".jpg"):
            raise ValueError("Expected JPEG image!")

        with open(self.file_path, "rb") as file:
            self.image_data = base64.b64encode(file.read())

        return self

    @model_serializer
    def serialize_to_bytes(self) -> bytes:
        assert self.image_data is not None
        return self.image_data


class AddCustomPlaylistCoverImageRequest(
    RequestModel[AddCustomPlaylistCoverImageRequestParams, AddCustomPlaylistCoverImageRequestBody]
):
    method_type: HTTPMethod = HTTPMethod.PUT
