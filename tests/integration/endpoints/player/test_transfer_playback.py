import random

import pytest

from spotantic.endpoints.player import get_available_devices
from spotantic.endpoints.player import transfer_playback
from spotantic.models.player.requests import TransferPlaybackRequest


@pytest.mark.asyncio
@pytest.mark.affects_playback
@pytest.mark.requires_active_device
async def test_transfer_playback(client):
    available_devices_data = (await get_available_devices(client)).data
    device_ids = [device.device_id for device in available_devices_data if device.device_id is not None]
    if not device_ids:
        pytest.skip("No available devices to transfer playback to.")

    result = await transfer_playback(client, device_ids=[random.choice(device_ids)])

    assert isinstance(result.request, TransferPlaybackRequest)
    assert result.response is None or isinstance(result.response, bytes)
    assert result.data is None
