from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.shows import get_show
from spotantic.models.shows.requests import GetShowRequest
from spotantic.models.spotify import ShowModel


@pytest.mark.asyncio
async def test_get_show_builds_request_and_returns_parsed_data():
    client = mock.AsyncMock()
    fake_response = {"id": "s1"}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(id="s1")

    with (
        mock.patch.object(GetShowRequest, "build", return_value=request_obj) as build_mock,
        mock.patch.object(ShowModel, "model_validate", return_value=fake_model) as validate_mock,
    ):
        result = await get_show(client, show_id="s1", market="US")

        build_mock.assert_called_once_with(show_id="s1", market="US")
        client.request_json.assert_awaited_once_with(request_obj)
        validate_mock.assert_called_once_with(fake_response)

        assert result.request is request_obj
        assert result.response == fake_response
        assert result.data is fake_model
