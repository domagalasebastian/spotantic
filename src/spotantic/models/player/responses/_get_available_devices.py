from pydantic import BaseModel

from spotantic.models.spotify import DeviceModel


class GetAvailableDevicesResponse(BaseModel):
    """Response model for Get Available Devices endpoint."""

    devices: list[DeviceModel]
    """List of devices."""
