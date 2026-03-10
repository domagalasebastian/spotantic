from types import SimpleNamespace
from unittest import mock

import pytest

from spotantic.endpoints.player import get_available_devices
from spotantic.models.player.requests import GetAvailableDevicesRequest


@pytest.mark.asyncio
async def test_get_available_devices_builds_request_and_returns_devices():
    client = mock.AsyncMock()
    fake_response = [{"id": "d1"}, {"id": "d2"}]
    client.request_json.return_value = fake_response

    request_obj = object()
    fake_model = SimpleNamespace(devices=["d1", "d2"])

    with mock.patch.object(GetAvailableDevicesRequest, "build", return_value=request_obj) as build_mock:
        with mock.patch(
            "spotantic.models.player.responses.GetAvailableDevicesResponse.model_validate", return_value=fake_model
        ) as validate_mock:
            result = await get_available_devices(client)

            build_mock.assert_called_once_with()
            client.request_json.assert_awaited_once_with(request_obj)
            validate_mock.assert_called_once_with(fake_response)

            assert result.request is request_obj
            assert result.response == fake_response
            assert result.data == fake_model.devices
