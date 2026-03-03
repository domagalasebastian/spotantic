from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.albums import get_user_saved_albums
from spotantic.models.albums.requests import GetUserSavedAlbumsRequest
from spotantic.models.spotify import PagedResultModel


@pytest.mark.asyncio
async def test_get_user_saved_albums_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"items": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    paged_model = SimpleNamespace(items=[], limit=20, offset=0)

    with (
        mock.patch.object(GetUserSavedAlbumsRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(PagedResultModel, "model_validate", return_value=paged_model) as validate_mock,
    ):
        result = await get_user_saved_albums(client, limit=10, offset=0, market="US")

        build_mock.assert_called_once_with(limit=10, offset=0, market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is paged_model
