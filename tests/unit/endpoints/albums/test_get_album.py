from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.albums import get_album
from spotantic.models.albums.requests import GetAlbumRequest
from spotantic.models.spotify import AlbumModel


@pytest.mark.asyncio
async def test_get_album_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"id": "album123"}
    client.request_json.return_value = fake_response

    request_obj = object()
    album_model = SimpleNamespace(id="album123")

    with (
        mock.patch.object(GetAlbumRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(AlbumModel, "model_validate", return_value=album_model) as validate_mock,
    ):
        result = await get_album(client, album_id="album123", market="US")

        build_mock.assert_called_once_with(album_id="album123", market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is album_model
