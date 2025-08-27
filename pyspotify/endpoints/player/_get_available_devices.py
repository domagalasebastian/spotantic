from typing import List

from pyspotify.client import PySpotifyClient
from pyspotify.custom_types import APIResponse
from pyspotify.models import APICallModel
from pyspotify.models.player.requests import GetAvailableDevicesRequest
from pyspotify.models.spotify import DeviceModel


async def get_available_devices(
    client: PySpotifyClient,
) -> APICallModel[GetAvailableDevicesRequest, APIResponse, List[DeviceModel]]:
    request = GetAvailableDevicesRequest(
        endpoint="me/player/devices",
    )
    response = await client.request(request)
    assert response is not None
    data = [DeviceModel(**device_data) for device_data in response["devices"]]

    return APICallModel(request=request, response=response, data=data)
