from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.shows import get_several_shows
from spotantic.models.shows.requests import GetSeveralShowsRequest
from spotantic.models.shows.responses import GetSeveralShowsResponse


@pytest.mark.asyncio
async def test_get_several_shows_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"shows": []}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(shows=[])

    with (
        mock.patch.object(GetSeveralShowsRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(GetSeveralShowsResponse, "model_validate", return_value=fake_model) as validate_mock,
    ):
        result = await get_several_shows(client, show_ids=["s1", "s2"], market="US")

        build_mock.assert_called_once_with(show_ids=["s1", "s2"], market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is fake_model.shows
