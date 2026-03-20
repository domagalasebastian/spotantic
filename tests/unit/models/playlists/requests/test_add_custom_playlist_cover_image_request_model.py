import base64
from http import HTTPMethod

import pytest
from pydantic import ValidationError

from spotantic.models.playlists.requests import AddCustomPlaylistCoverImageRequest
from spotantic.models.playlists.requests import AddCustomPlaylistCoverImageRequestBody
from spotantic.models.playlists.requests import AddCustomPlaylistCoverImageRequestParams
from spotantic.types import AuthScope
from spotantic.types import SpotifyItemID


def test_add_custom_playlist_cover_image_request_model_uses_image_data_bytes(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    image_data = b"abc"

    req = AddCustomPlaylistCoverImageRequest.build(playlist_id=example_id, image_data=image_data)

    assert req.endpoint == f"playlists/{example_id}/images"
    assert req.method_type is HTTPMethod.PUT
    assert req.headers.content_type == "image/jpeg"
    assert AuthScope.PLAYLIST_MODIFY_PRIVATE in req.required_scopes
    assert AuthScope.PLAYLIST_MODIFY_PUBLIC in req.required_scopes
    assert AuthScope.UGC_IMAGE_UPLOAD in req.required_scopes

    body = req.body
    assert isinstance(body, AddCustomPlaylistCoverImageRequestBody)
    assert body.image_data == image_data
    assert body.to_http_body() == image_data

    params = req.params
    assert isinstance(params, AddCustomPlaylistCoverImageRequestParams)
    assert params.playlist_id == example_id


def test_add_custom_playlist_cover_image_request_model_loads_image_from_file(
    tmp_path, example_instances_of_type
) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    raw_bytes = b"\xff\xd8\xff"
    file_path = tmp_path / "cover.jpg"
    file_path.write_bytes(raw_bytes)

    req = AddCustomPlaylistCoverImageRequest.build(playlist_id=example_id, file_path=file_path)

    expected_base64 = base64.b64encode(raw_bytes)
    assert isinstance(req.body, AddCustomPlaylistCoverImageRequestBody)
    assert req.body.image_data == expected_base64
    assert req.body.to_http_body() == expected_base64


def test_add_custom_playlist_cover_image_request_model_requires_image_data_or_file(example_instances_of_type) -> None:
    example_id = example_instances_of_type[SpotifyItemID]

    with pytest.raises(ValidationError):
        AddCustomPlaylistCoverImageRequest.build(playlist_id=example_id)


def test_add_custom_playlist_cover_image_request_model_rejects_non_jpeg_file(
    tmp_path, example_instances_of_type
) -> None:
    example_id = example_instances_of_type[SpotifyItemID]
    file_path = tmp_path / "cover.png"
    file_path.write_bytes(b"notajpeg")

    with pytest.raises(ValidationError):
        AddCustomPlaylistCoverImageRequest.build(playlist_id=example_id, file_path=file_path)
