from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class DeviceModel(BaseModel):
    model_config = ConfigDict(serialize_by_alias=True)

    device_id: Optional[str] = Field(None, alias="id")
    is_active: bool
    is_private_session: bool = Field(repr=False)
    is_restricted: bool
    device_name: str = Field(alias="name")
    device_type: str = Field(alias="type")
    volume_percent: Optional[int]
    supports_volume: bool
