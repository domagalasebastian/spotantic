from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.albums import get_new_releases
from spotantic.models.albums.requests import GetNewReleasesRequest
from spotantic.models.albums.responses import GetNewReleasesResponse


@pytest.mark.asyncio
async def test_get_new_releases_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"albums": {"items": []}}
    client.request_json.return_value = fake_response

    request_obj = object()
    albums_container = SimpleNamespace(albums=SimpleNamespace(items=[], limit=20, offset=0))

    with (
        mock.patch.object(GetNewReleasesRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(GetNewReleasesResponse, "model_validate", return_value=albums_container) as validate_mock,
    ):
        result = await get_new_releases(client, limit=5, offset=0)

        build_mock.assert_called_once_with(limit=5, offset=0)
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is albums_container.albums
