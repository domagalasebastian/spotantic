from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.player import get_user_queue
from spotantic.models.player.requests import GetUserQueueRequest


@pytest.mark.asyncio
async def test_get_user_queue_builds_request_and_returns_model():
    client = mock.AsyncMock()
    fake_response = {"dummy": "value"}
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(dummy="value")

    with mock.patch.object(GetUserQueueRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.player.responses.GetUserQueueResponse.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await get_user_queue(client)

            build_mock.assert_called_once_with()
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data is fake_model
