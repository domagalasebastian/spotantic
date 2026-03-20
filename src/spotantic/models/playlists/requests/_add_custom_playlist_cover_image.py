from __future__ import annotations

import base64
from http import HTTPMethod
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import FilePath
from pydantic import model_validator

from spotantic.models import RequestBodyModel
from spotantic.models import RequestHeadersModel
from spotantic.models import RequestModel
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


class AddCustomPlaylistCoverImageRequestParams(BaseModel):
    """Params model for Add Custom Playlist Cover Image request."""

    model_config = ConfigDict(serialize_by_alias=True)

    playlist_id: SpotifyItemID = Field(serialization_alias="id")
    """The Spotify ID of the playlist."""


class AddCustomPlaylistCoverImageRequestBody(RequestBodyModel):
    """Body model for Add Custom Playlist Cover Image request."""

    image_data: Optional[bytes] = None
    """The image data as bytes."""

    file_path: Optional[FilePath] = None
    """The file path to a JPEG image."""

    @model_validator(mode="after")
    def get_image_data_from_file(self) -> AddCustomPlaylistCoverImageRequestBody:
        """Loads image data from file if `file_path` is provided and `image_data` is None.

        Returns:
            The validated model with `image_data` populated.

        Raises:
            ValueError: If neither `image_data` nor `file_path` is provided. Or if the file is not a JPEG image.
        """
        if self.image_data is not None:
            return self

        if self.file_path is None:
            raise ValueError("Either `image_data` or `file_path` must be provided!")

        if self.file_path.suffix not in (".jpeg", ".jpg"):
            raise ValueError("Expected JPEG image!")

        with open(self.file_path, "rb") as file:
            self.image_data = base64.b64encode(file.read())

        return self

    def to_http_body(self) -> Optional[Union[str, bytes]]:
        """Converts the model to the appropriate HTTP body format.

        For this request, the body should be the raw image data as bytes.

        Returns:
            The image data as bytes, or None if no image data is available.
        """
        return self.image_data


class AddCustomPlaylistCoverImageRequest(
    RequestModel[AddCustomPlaylistCoverImageRequestParams, AddCustomPlaylistCoverImageRequestBody]
):
    """Request model for Add Custom Playlist Cover Image endpoint."""

    required_scopes: set[AuthScope] = {
        AuthScope.PLAYLIST_MODIFY_PRIVATE,
        AuthScope.PLAYLIST_MODIFY_PUBLIC,
        AuthScope.UGC_IMAGE_UPLOAD,
    }
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    headers: RequestHeadersModel = RequestHeadersModel(content_type="image/jpeg")
    """Headers for the request."""

    @classmethod
    def build(
        cls,
        *,
        playlist_id: SpotifyItemID,
        image_data: Optional[bytes] = None,
        file_path: Optional[FilePath] = None,
    ) -> AddCustomPlaylistCoverImageRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            playlist_id: The Spotify ID of the playlist.
            image_data: The image data as bytes. Must be a JPEG image, maximum size 256 KB.
            file_path: The file path to a JPEG image. Must be maximum size 256 KB.

        Returns:
            Validated Request object.
        """
        params = AddCustomPlaylistCoverImageRequestParams(playlist_id=playlist_id)
        body = AddCustomPlaylistCoverImageRequestBody(image_data=image_data, file_path=file_path)
        endpoint = f"playlists/{playlist_id}/images"

        return cls(endpoint=endpoint, params=params, body=body)
