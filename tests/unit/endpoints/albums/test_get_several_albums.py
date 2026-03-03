from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.albums import get_several_albums
from spotantic.models.albums.requests import GetSeveralAlbumsRequest
from spotantic.models.albums.responses import GetSeveralAlbumsResponse


@pytest.mark.asyncio
async def test_get_several_albums_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"albums": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    response_model = SimpleNamespace(albums=[SimpleNamespace(id="a1"), SimpleNamespace(id="a2")])

    with (
        mock.patch.object(GetSeveralAlbumsRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(GetSeveralAlbumsResponse, "model_validate", return_value=response_model) as validate_mock,
    ):
        result = await get_several_albums(client, album_ids=["a1", "a2"], market=None)

        build_mock.assert_called_once_with(album_ids=["a1", "a2"], market=None)
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is response_model.albums
