from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.albums import get_album_tracks
from spotantic.models.albums.requests import GetAlbumTracksRequest
from spotantic.models.spotify import PagedResultModel


@pytest.mark.asyncio
async def test_get_album_tracks_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"items": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    paged_model = SimpleNamespace(items=[], limit=20, offset=0)

    with (
        mock.patch.object(GetAlbumTracksRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(PagedResultModel, "model_validate", return_value=paged_model) as validate_mock,
    ):
        result = await get_album_tracks(client, album_id="album123", limit=10, offset=0, market="US")

        build_mock.assert_called_once_with(album_id="album123", limit=10, offset=0, market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is paged_model
