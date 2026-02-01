from __future__ import annotations

from http import HTTPMethod
from typing import Annotated
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from pyspotify.custom_types import Scope
from pyspotify.models import RequestModel


class SetPlaybackVolumeRequestParams(BaseModel):
    """Params model for Set Playback Volume request."""

    volume_percent: Annotated[int, Field(ge=0, le=100)]
    """The volume to set. Must be a value from 0 to 100 inclusive."""

    device_id: Optional[str] = None
    """The id of the device this command is targeting."""


class SetPlaybackVolumeRequest(RequestModel[SetPlaybackVolumeRequestParams, None]):
    """Request model for Set Playback Volume endpoint."""

    required_scopes: set[Scope] = {Scope.USER_MODIFY_PLAYBACK_STATE}
    """Required authorization scopes for the request."""

    method_type: HTTPMethod = HTTPMethod.PUT
    """HTTP method for the request."""

    endpoint: Optional[str] = "me/player/volume"
    """Endpoint associated with the request."""

    @classmethod
    def build(
        cls,
        *,
        volume_percent: int,
        device_id: Optional[str] = None,
    ) -> SetPlaybackVolumeRequest:
        """Builds a request model based on given parameters.

        The function automatically determines the endpoint if it is not static.
        Also, it automatically assigns parameters to request query or body.

        Args:
            volume_percent: The volume to set. Must be a value from 0 to 100 inclusive.
            device_id: The id of the device this command is targeting.

        Returns:
            Validated Request object.
        """
        params = SetPlaybackVolumeRequestParams(
            volume_percent=volume_percent,
            device_id=device_id,
        )

        return cls(params=params)
