import pytest

from spotantic.endpoints.player import get_available_devices
from spotantic.models.player.requests import GetAvailableDevicesRequest
from spotantic.models.spotify import DeviceModel


@pytest.mark.asyncio
@pytest.mark.readonly
async def test_get_available_devices(client):
    result = await get_available_devices(client)

    assert isinstance(result.request, GetAvailableDevicesRequest)
    assert isinstance(result.response, dict)
    assert isinstance(result.data, list)
    assert all(isinstance(device, DeviceModel) for device in result.data)
