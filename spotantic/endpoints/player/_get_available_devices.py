from spotantic.client import SpotanticClient
from spotantic.models import APICallModel
from spotantic.models.player.requests import GetAvailableDevicesRequest
from spotantic.models.spotify import DeviceModel
from spotantic.types import APIResponse


async def get_available_devices(
    client: SpotanticClient,
) -> APICallModel[GetAvailableDevicesRequest, APIResponse, list[DeviceModel]]:
    """Get information about a user’s available Spotify Connect devices.

    Some device models are not supported and will not be listed in the API response.

    Args:
        client: :class:`~spotantic.client.SpotanticClient` instance.

    Returns:
        An object containing the request used to obtain the response, the retrieved data and
        parsed data as model.
    """
    request = GetAvailableDevicesRequest.build()
    response = await client.request(request)
    assert response is not None
    data = [DeviceModel(**device_data) for device_data in response["devices"]]

    return APICallModel(request=request, response=response, data=data)
