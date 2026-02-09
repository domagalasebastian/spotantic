from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class DeviceModel(BaseModel):
    """Model representing information about an user’s Spotify Connect device."""

    model_config = ConfigDict(serialize_by_alias=True)

    device_id: Optional[str] = Field(None, alias="id")
    """The device ID. This ID is unique and persistent to some extent."""

    is_active: bool
    """If this device is the currently active device."""

    is_private_session: bool = Field(repr=False)
    """If this device is currently in a private session."""

    is_restricted: bool
    """Whether controlling this device is restricted. At present if this is `True` then
    no Web API commands will be accepted by this device."""

    device_name: str = Field(alias="name")
    """A human-readable name for the device."""

    device_type: str = Field(alias="type")
    """A device type."""

    volume_percent: Optional[int] = None
    """The current volume in percent."""

    supports_volume: bool
    """If this device can be used to set the volume."""
